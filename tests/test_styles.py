"""Tests for registration of packaged Matplotlib styles."""

from importlib.resources import as_file, files

import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

import yieldplotlib

STYLE_FILES = [
    path
    for path in files(yieldplotlib).joinpath("style").iterdir()
    if path.name.endswith(".mplstyle")
]


@pytest.mark.parametrize("style_file", STYLE_FILES, ids=lambda path: path.name)
def test_packaged_style_registered(style_file):
    """Importing yieldplotlib makes every packaged style usable by name."""
    with as_file(style_file) as path, mpl.rc_context():
        expected = mpl.rc_params_from_file(path, use_default_template=False)
        assert expected
        plt.style.use("default")
        plt.style.use(path.stem)
        for key, value in expected.items():
            assert mpl.rcParams[key] == value
