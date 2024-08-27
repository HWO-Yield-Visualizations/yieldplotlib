"""Loader for EXOSIMS data, organizing files into a directory-based structure."""

from pathlib import Path

from tqdm import tqdm

from yieldplotlib.core.csv_node import CSVNode
from yieldplotlib.core.data_node import DataNode
from yieldplotlib.core.directory_node import DirectoryNode
from yieldplotlib.load.exosims import DRMNode, EXOSIMSInputNode, SPCNode


class EXOSIMSDirectory(DirectoryNode):
    """Loader for EXOSIMS data, organizing files into a directory-based structure."""

    def __init__(self, root_directory: Path):
        """Initialize the EXOSIMSLoader by scanning the directory structure."""
        super().__init__(root_directory)

    def load(self):
        """Override the load method to handle EXOSIMS-specific files."""
        paths = list(self.directory_path.iterdir())
        with tqdm(
            total=len(paths),
            desc=f"Loading EXOSIMS directory {self.directory_path.name}",
            unit="item",
        ) as pbar:
            for path in self.directory_path.iterdir():
                if path.is_dir():
                    # Recursively handle subdirectories by creating
                    # EXOSIMSDirectory nodes
                    exosims_directory = EXOSIMSDirectory(path)
                    self.add(exosims_directory)
                else:
                    # Create EXOSIMS-specific file nodes
                    self.add(self._create_file_node(path))
                pbar.update(1)

    def _create_file_node(self, path: Path) -> DataNode:
        """Override file node creation logic for EXOSIMS-specific files."""
        if path.suffix == ".pkl" and path.parts[-2] == "drm":
            return DRMNode(path)
        elif path.suffix == ".spc" and path.parts[-2] == "spc":
            return SPCNode(path)
        elif path.suffix == ".csv":
            return CSVNode(path)
        elif path.suffix == ".json":
            return EXOSIMSInputNode(path)
        return None
