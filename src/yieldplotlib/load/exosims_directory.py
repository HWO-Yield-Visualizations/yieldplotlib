"""Loader for EXOSIMS data, organizing files into a directory-based structure."""

from pathlib import Path

import numpy as np

from yieldplotlib.core import DirectoryNode, Node
from yieldplotlib.load.exosims import DRMFile, EXOSIMSCSVFile, EXOSIMSInputFile, SPCFile
from yieldplotlib.logger import logger


class EXOSIMSDirectory(DirectoryNode):
    """Loader for EXOSIMS data, organizing files into a directory-based structure."""

    def __init__(self, root_directory: Path):
        """Initialize the EXOSIMSLoader by scanning the directory structure."""
        super().__init__(root_directory)
        # After loading all data check that the root
        if self.__class__.__name__ == "EXOSIMSDirectory":
            # If all paths are local, we can don't need to filter the target list
            if not self.input.all_local_paths:
                # Match the loaded target list object's stars to the stars in the
                # csv files
                csv_stars = self.get("star_name")
                has_TL = hasattr(self.input, "TL")
                if has_TL:
                    # Filter TL to only include stars in the csv files
                    sInds = np.where(np.isin(self.input.TL.Name, csv_stars))[0]
                    self.input.TL.revise_lists(sInds)

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
