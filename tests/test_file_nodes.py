"""Tests for file node resource ownership."""

import gc
import warnings

import astropy.io.fits as fits
import numpy as np

from yieldplotlib.core.file_nodes import FitsFile


def test_fits_file_releases_handles(tmp_path):
    """FITS data survives closing the source without leaking file handles."""
    path = tmp_path / "example.fits"
    data = np.arange(12).reshape(3, 4)
    fits.PrimaryHDU(data, header=fits.Header({"EXAMPLE": 42})).writeto(path)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", ResourceWarning)
        node = FitsFile(path)
        np.testing.assert_array_equal(node.fits_file[0].data, data)
        assert node.fits_file[0].header["EXAMPLE"] == 42
        del node
        gc.collect()

    assert not caught, [str(warning.message) for warning in caught]
