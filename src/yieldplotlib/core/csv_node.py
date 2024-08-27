"""Base module for all CSV file nodes."""

from pathlib import Path

import pandas as pd

from yieldplotlib.core.data_node import DataNode


class CSVNode(DataNode):
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
