"""Node for handling JSON files and their associated data."""

import json
from pathlib import Path

from yieldplotlib.core.data_node import DataNode


class JSONNode(DataNode):
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
