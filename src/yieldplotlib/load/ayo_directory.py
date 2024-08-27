"""Loaders for AYO directories containing multiple file types."""

from pathlib import Path

from yieldplotlib.core.directory_node import DirectoryNode

# BUG: This is a placeholder to make imports work correctly. Copy the
# EXOSIMSDirectory format to make it work correctly.


class AYODirectory(DirectoryNode):
    """Loader for AYO directories.

    Currently only supports CSV files.

    Args:
        directory (str):
            The path to the directory containing AYO files.
    """

    def __init__(self, directory: str):
        """Initialize the AYODirectoryLoader.

        Args:
            directory (str):
                The path to the directory containing AYO files
        """
        super().__init__()
        self.directory = Path(directory)
        self._scan_directory()
