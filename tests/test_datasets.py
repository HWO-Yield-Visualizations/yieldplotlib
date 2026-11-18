"""Tests for the datasets module."""

from yippy import YIPPackage

from yieldplotlib.datasets import fetch_ayo_data, fetch_exosims_data, fetch_yip_data


def test_fetch_ayo_data():
    """Test that AYO data can be fetched and loaded."""
    ayo = fetch_ayo_data()
    assert ayo is not None
    # Simple sanity check that the data is loaded
    assert ayo.get("star_dist") is not None


def test_fetch_exosims_data():
    """Test that EXOSIMS data can be fetched and loaded."""
    exosims = fetch_exosims_data()
    assert exosims is not None
    # Simple sanity check that the data is loaded
    assert exosims.get("star_dist") is not None


def test_fetch_yip_data():
    """Test that YIP data can be fetched and loaded."""
    yip = fetch_yip_data()
    assert isinstance(yip, YIPPackage)
    assert yip.offsets_xy_lod.shape == (len(yip.offaxis_psfs), 2)
