"""The abstract base class for all nodes (files and directories)."""

from abc import ABC, abstractmethod
from pathlib import Path


class Node(ABC):
    """Abstract base class for all nodes (files and directories)."""

    def __init__(self, file_path: Path):
        """Initialize the node with a reference to the data."""
        self.data = None
        self.file_path = file_path
        self.file_name = file_path.name

    @abstractmethod
    def load(self):
        """Load the file data or trigger recursive loading for directories."""
        pass

    @abstractmethod
    def get(self, key: str):
        """Abstract method to search for data associated with a key."""
        pass

    def has_key(self, key: str) -> bool:
        """Abstract method to determine if the node contains the given key."""
        return False

    def __repr__(self):
        """Default representation for a DataNode."""
        return f"<{self.__class__.__name__}: {self.file_name}>"

    def display_tree(self, level=0, max_children=5, prefix=""):
        """Default display method for a DataNode."""
        return f"{prefix}{self.__repr__()}\n"
