"""Base module for all common file-type nodes."""

import json
import pickle
import re
from pathlib import Path

import pandas as pd

from yieldplotlib.core.node import Node
from yieldplotlib.key_map import KEY_MAP
from yieldplotlib.logger import logger


class FileNode(Node):
    """A generic node for handling files."""

    def __init__(self, file_path: Path):
        """Initialize the node with the file path."""
        super().__init__(file_path)
        self.load()
        self.expected_keys = self.get_expected_keys()

    def translate_key(self, key: str) -> str:
        """Translate the standardized key to the file-specific key."""
        return KEY_MAP.get(key, {}).get(self.__class__.__name__, key)

    def get_expected_keys(self):
        """Get a list of keys expected to be in this file based on the key map."""
        expected_keys = []
        for key, mappings in KEY_MAP.items():
            if self.__class__.__name__ in mappings:
                expected_keys.append(mappings[self.__class__.__name__])
        return expected_keys

    def has_key(self, key: str) -> bool:
        """Check if the file contains the given key."""
        translated_key = self.translate_key(key)
        return translated_key in self.expected_keys

    def get(self, key: str):
        """Translate the key and delegate to the subclass-specific _get method."""
        translated_key = self.translate_key(key)
        has_key = translated_key in self.expected_keys
        if has_key:
            # Check if the key is mapped to a specific filename
            required_filename = getattr(self, "KEY_FILENAME_MAP", {}).get(key)
            if required_filename:
                if isinstance(required_filename, str):
                    if not self._filename_matches(required_filename):
                        # Skip this file if the required filename does not match
                        logger.debug(f"Key {key} requires {required_filename}.")
                        return None
            logger.info(f"Key {key} found in {self.file_name}.")
            data = self._get(translated_key)
            return self.transform_data(key, data)
        else:
            logger.debug(f"Key {key} not found in {self.file_name}.")
            return None

    def _get(self, translated_key: str):
        """Subclass-specific method to retrieve the data associated with the key."""
        raise NotImplementedError("Subclasses must implement the _get method.")

    def transform_data(self, key: str, data):
        """Apply key-specific data transformations defined in the subclass."""
        transform_func = getattr(self, f"transform_{key}", None)
        if callable(transform_func):
            return transform_func(data)
        return data

    def _filename_matches(self, pattern: str) -> bool:
        """Check if the file name matches the pattern, either as a string or regex."""
        # If pattern is a direct match
        if pattern == self.file_path.name:
            return True
        # If pattern is a regex match
        if re.match(pattern, self.file_path.name):
            return True
        return False


class CSVFile(FileNode):
    """Represents a CSV file and its associated data."""

    def __init__(self, file_path: Path):
        """Initialize the CSV node with the file path."""
        super().__init__(file_path)
        self.load()

    def load(self):
        """Load the CSV file into memory."""
        self.data = pd.read_csv(self.file_path)

    def _get(self, key: str):
        """Return the data associated with the key."""
        if key in self.data.columns:
            return self.data[key]
        return None


class JSONFile(FileNode):
    """Node for handling JSON files and their associated data."""

    def __init__(self, file_path: Path):
        """Initialize the node with the file path and load."""
        super().__init__(file_path)
        self.load()

    def load(self):
        """Load the JSON file into memory."""
        with open(self.file_path, "r") as f:
            self.data = json.load(f)

    def _get(self, key: str):
        """Return the data associated with the key."""
        return self.data.get(key, None)


class PickleFile(FileNode):
    """Node for handling generic pickle files and their associated data."""

    def __init__(self, file_path: Path):
        """Initialize the node with the file path."""
        super().__init__(file_path)
        self.load()

    def load(self):
        """Load the pickle file into memory."""
        with open(self.file_path, "rb") as f:
            self.data = pickle.load(f)

    def _get(self, key: str):
        """Return the data associated with the key."""
        return self.data.get(key, None)
