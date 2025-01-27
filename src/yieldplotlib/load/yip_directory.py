"""Loader for YIP data, organizing files into a directory-based structure."""

from pathlib import Path

import astropy.io.fits as pyfits
from yippy.coronagraph import Coronagraph

from yieldplotlib.core import DirectoryNode, Node
from yieldplotlib.core.file_nodes import FitsFile


class YIPDirectory(DirectoryNode):
    """Loader for YIPs, organizing files into a directory-based structure."""

    def __init__(self, root_directory: Path):
        """Initialize the loader by scanning the directory structure."""
        super().__init__(root_directory)
        self.coronagraph = Coronagraph(root_directory, use_jax=False)

    def _create_directory_node(self, path: Path) -> Node:
        """Override directory node creation logic for YIP-specific directories."""
        return self.create_base_directory(path)

    def _create_file_node(self, path: Path) -> Node:
        """Override file node creation logic for YIP-specific files."""
        if path.suffix == ".fits":
            return FitsFile(path)
        else:
            return self.create_base_file(path)

    def get(self, key: str):
        """Search for a key (e.g., "data" or "D") in the tree structure."""
        if key.endswith(".data"):
            if key == "offax.data":
                return pyfits.getdata(Path(self.coronagraph.yip_path, "offax_psf.fits"))
            elif key == "offax_offset_list.data":
                return pyfits.getdata(
                    Path(self.coronagraph.yip_path, "offax_psf_offset_list.fits")
                )
            elif key == "stellar_intens.data":
                return pyfits.getdata(
                    Path(self.coronagraph.yip_path, "stellar_intens.fits")
                )
            elif key == "stellar_intens_diam_list.data":
                return pyfits.getdata(
                    Path(self.coronagraph.yip_path, "stellar_intens_diam_list.fits")
                )
            elif key == "sky_trans.data":
                return pyfits.getdata(Path(self.coronagraph.yip_path, "sky_trans.fits"))
        else:
            return getattr(self.coronagraph, key)
