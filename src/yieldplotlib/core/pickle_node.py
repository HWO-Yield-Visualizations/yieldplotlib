"""A generic node for handling pickle files."""

import pickle
from pathlib import Path

from yieldplotlib.core.data_node import DataNode


class PickleNode(DataNode):
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
