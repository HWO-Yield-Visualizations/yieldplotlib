"""Loader for YIP data, organizing files into a directory-based structure."""


from pathlib import Path
from yieldplotlib.core import DirectoryNode, Node
from yieldplotlib.core.file_nodes import FitsFile


class YIPDirectory(DirectoryNode):
    """Loader for yield input packages, organizing files into a directory-based structure."""

    def __init__(self, root_directory: Path):
        """Initialize the EXOSIMSLoader by scanning the directory structure."""
        super().__init__(root_directory)

    def _create_directory_node(self, path: Path) -> Node:
        """Override directory node creation logic for EXOSIMS-specific directories."""
        return self.create_base_directory(path)

    def _create_file_node(self, path: Path) -> Node:
        """Override file node creation logic for EXOSIMS-specific files."""
        if path.suffix == ".fits":
            return FitsFile(path)
        else:
            return self.create_base_file(path)

    def get(self, key: str):
        """Search for a key (e.g., star_distances) in the tree structure."""
        for file in self._children:
            if (file.file_name == "offax_psf.fits"
                    and key == "offax_psf"):
                return file.get("data")
            elif (file.file_name == "offax_psf_offset_list.fits"
                  and key == "offax_psf_offset_list"):
                return file.get("data")
            elif (file.file_name == "sky_trans.fits"
                  and key == "sky_trans"):
                return file.get("data")
            elif (file.file_name == "stellar_intens.fits"
                  and key == "stellar_intens"):
                return file.get("data")
            elif (file.file_name == "stellar_intens_diam_list.fits"
                  and key == "stellar_intens_diam_list"):
                return file.get("data")
        return None
