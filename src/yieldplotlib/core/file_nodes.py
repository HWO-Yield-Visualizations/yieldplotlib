"""Base module for all common file-type nodes."""

import json
import pickle
from pathlib import Path

import pandas as pd

from yieldplotlib.core.node import Node


class FileNode(Node):
    """A generic node for handling files."""

    def __init__(self, file_path: Path):
        """Initialize the node with the file path."""
        super().__init__(file_path)
        self.load()


class CSVFile(FileNode):
    """Represents a CSV file and its associated data."""

    def __init__(self, file_path: Path):
        """Initialize the CSV node with the file path."""
        super().__init__(file_path)
        self.load()

    def load(self):
        """Load the CSV file into memory."""
        self.data = pd.read_csv(self.file_path)

    def get(self, key: str):
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

    def get(self, key: str):
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

    def get(self, key: str):
        """Return the data associated with the key."""
        return self.data.get(key, None)
