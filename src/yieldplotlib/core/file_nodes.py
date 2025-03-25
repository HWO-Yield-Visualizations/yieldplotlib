"""Base module for all common file-type nodes."""

import json
import pickle
import posixpath
from pathlib import Path

import astropy.io.fits as pyfits
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
        self.file_key_map, self.file_transforms = self.get_file_key_map()

    def get_file_key_map(self):
        """Get a list of keys expected to be in this file based on the key map."""
        file_key_map = {}
        transforms = {}
        for key, mappings in KEY_MAP.items():
            if self.__class__.__name__ in mappings:
                filename = mappings[self.__class__.__name__]["file"]
                key_name = mappings[self.__class__.__name__]["name"]
                transform = mappings[self.__class__.__name__]["transform"]
                matching_file = self.file_name.endswith(filename)
                if matching_file:
                    file_key_map[key] = key_name
                    transforms[key] = transform
        return file_key_map, transforms

    def get(self, key: str, **kwargs):
        """Translate the key and delegate to the subclass-specific _get method."""
        # translated_key = self.translate_key(key)
        has_key = key in self.file_key_map.keys()
        if has_key:
            logger.debug(f"Key {key} found in {self.file_name}.")
            data = self._get(self.file_key_map[key], **kwargs)
            return self.transform_data(key, data, **kwargs)
        else:
            logger.debug(f"Key {key} not found in {self.file_name}.")
            return None

    def _get(self, translated_key: str, **kwargs):
        """Subclass-specific method to retrieve the data associated with the key.

        Args:
            translated_key: The key to look up in the data.
            **kwargs: Additional arguments that may be used by specific implementations.
        """
        raise NotImplementedError("Subclasses must implement the _get method.")

    def transform_data(
        self, key: str, data, type_override=None, value_override=None, **kwargs
    ):
        """Apply key-specific data transformations defined in the subclass."""
        _type = self.file_transforms[key]["type"]
        _val = self.file_transforms[key]["value"]
        if type_override is not None:
            _type = type_override
            _val = value_override
        else:
            _type = self.file_transforms[key]["type"]
            _val = self.file_transforms[key]["value"]

        match _type:
            case "none":
                return data
            case "custom":
                transform_func = getattr(self, f"transform_{key}", None)
                if callable(transform_func):
                    return transform_func(data)
                else:
                    raise NotImplementedError(
                        f"Custom transform for {key} notimplemented."
                    )
            case "index":
                return data[_val]
            case "sum":
                return data.sum()
            case _:
                raise NotImplementedError(f"Transform type {_type} not implemented.")


class CSVFile(FileNode):
    """Represents a CSV file and its associated data."""

    def __init__(self, file_path: Path):
        """Initialize the CSV node with the file path."""
        super().__init__(file_path)
        self.load()

    def load(self):
        """Load the CSV file into memory."""
        self.data = pd.read_csv(self.file_path)
        # Strip whitespace from column names
        self.data.columns = self.data.columns.str.strip()

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        if key in self.data.columns:
            return self.data[key].values
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

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        values = {}

        def json_recur(data, target_key):
            if isinstance(data, dict):
                for k, v in data.items():
                    if k == target_key:
                        try:
                            values[data["name"]] = data.get(key, None)
                        except KeyError:
                            values[data["instName"]] = data.get(key, None)
                    elif isinstance(v, (dict, list)):
                        json_recur(v, target_key)
            elif isinstance(data, list):
                for item in data:
                    json_recur(item, target_key)
            return values

        if self.data.get(key):
            return self.data.get(key)
        else:
            try:
                return json_recur(self.data, key)
            except KeyError:
                return None


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

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        return self.data.get(key, None)


class FitsFile(FileNode):
    """Node for handling generic fits files and their associated data."""

    def __init__(self, file_path: Path):
        """Initialize the node with the file path."""
        super().__init__(file_path)
        self.load()
        self.file_name = posixpath.basename(file_path)

    def load(self):
        """Load the fits file."""
        self.fits_file = pyfits.open(self.file_path)

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        if key == "data":
            return pyfits.getdata(self.file_path)
        else:
            return pyfits.getheader(self.file_path).get(key, None)
