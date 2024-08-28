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

    # def _scan_directory(self, current_directory: Path):
    #     """Recursively scan directories and build the directory tree."""
    #     for path in current_directory.iterdir():
    #         if path.is_dir():
    #             directory_node = DirectoryNode()
    #             self.add(directory_node)
    #             self._scan_directory(path)
    #         else:
    #             if path.suffix == ".csv":
    #                 self.add(CSVNode(path))
    #             elif path.suffix == ".pickle" and "drm" in path.stem:
    #                 self.add(DRMNode(path))
    #             elif path.suffix == ".pickle" and "spc" in path.stem:
    #                 self.add(SPCNode(path))
    #
    # def get(self, key: str):
    #     """Search for a key (e.g., star_distances) in the tree structure."""
    #     return super().get(key)
