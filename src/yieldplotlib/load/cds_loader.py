"""Loader for CDS data, organizing files into a directory-based structure."""

from pathlib import Path

from yieldplotlib.core.directory_node import DirectoryNode

# BUG: This is a placeholder to make imports work correctly.


class CDSDirectory(DirectoryNode):
    """Loader for CDS data, organizing files into a directory-based structure."""

    def __init__(self, root_directory: str):
        """Initialize the EXOSIMSLoader by scanning the directory structure."""
        super().__init__()
        self.root_directory = Path(root_directory)
        self._scan_directory(self.root_directory)
