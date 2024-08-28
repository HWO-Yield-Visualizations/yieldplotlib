"""Loaders for AYO directories containing multiple file types."""

from pathlib import Path

from yieldplotlib.core.directory_node import DirectoryNode
from yieldplotlib.core.node import Node
from yieldplotlib.load.ayo import AYOCSVFile


class AYODirectory(DirectoryNode):
    """Loader for AYO directories.

    Currently only supports CSV files.
    """

    def _create_file_node(self, path: Path) -> Node:
        """Override file node creation logic for AYO-specific files."""
        if path.suffix == ".csv":
            return AYOCSVFile(path)
        else:
            return self.create_base_file(path)
