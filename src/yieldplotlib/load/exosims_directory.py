"""Loader for EXOSIMS data, organizing files into a directory-based structure."""

from pathlib import Path

from yieldplotlib.core import DirectoryNode, Node
from yieldplotlib.load.exosims import DRMFile, EXOSIMSCSVFile, EXOSIMSInputFile, SPCFile
from yieldplotlib.logger import logger


class EXOSIMSDirectory(DirectoryNode):
    """Loader for EXOSIMS data, organizing files into a directory-based structure."""

    def __init__(self, root_directory: Path):
        """Initialize the EXOSIMSLoader by scanning the directory structure."""
        super().__init__(root_directory)

    def _create_directory_node(self, path: Path) -> Node:
        """Override directory node creation logic for EXOSIMS-specific directories."""
        if path.name == "drm":
            return DRMDirectory(path)
        elif path.name == "spc":
            return SPCDirectory(path)
        elif path.name == "csv":
            return EXOSIMSCSVDirectory(path)
        else:
            return self.create_base_directory(path)

    def _create_file_node(self, path: Path) -> Node:
        """Override file node creation logic for EXOSIMS-specific files."""
        if path.suffix == ".json":
            return EXOSIMSInputFile(path)
        else:
            return self.create_base_file(path)


class EXOSIMSCSVDirectory(EXOSIMSDirectory):
    """Loader for CSV data, organizing files into a directory-based structure."""

    def _create_file_node(self, path: Path):
        """Override file node creation logic for CSV-specific files."""
        if path.suffix == ".csv":
            return EXOSIMSCSVFile(path)
        else:
            logger.warning(
                (
                    f"Unexpected file type {path.suffix} for CSV directory. "
                    f"File {path.name}."
                )
            )
            return self.create_base_file(path)


class DRMDirectory(EXOSIMSDirectory):
    """Loader for DRM data, organizing files into a directory-based structure."""

    def _create_file_node(self, path: Path):
        """Override file node creation logic for DRM-specific files."""
        if path.suffix == ".pkl":
            return DRMFile(path)
        else:
            logger.warning(
                (
                    f"Unexpected file type {path.suffix} for DRM directory. "
                    f"File {path.name}."
                )
            )
            return self.create_base_file(path)


class SPCDirectory(EXOSIMSDirectory):
    """Loader for SPC data, organizing files into a directory-based structure."""

    def _create_file_node(self, path: Path):
        """Override file node creation logic for SPC-specific files."""
        if path.suffix == ".spc":
            return SPCFile(path)
        else:
            logger.warning(
                (
                    f"Unexpected file type {path.suffix} for SPC directory. "
                    f"File {path.name}."
                )
            )
            return self.create_base_file(path)
