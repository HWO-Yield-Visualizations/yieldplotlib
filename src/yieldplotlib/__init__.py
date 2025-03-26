"""yieldplotlib - A library for plotting yield data."""

__all__ = [
    "__version__",
    "fetch_ayo_data",
    "fetch_exosims_data",
    "KEY_MAP",
    "logger",
    "calculate_axis_limits_and_ticks",
    "get_nice_number",
    "subplots",
    "compare",
    "multi",
    "panel",
    "xy_grid",
]

import importlib.resources

import matplotlib.pyplot as plt

from ._version import __version__
from .datasets import fetch_ayo_data, fetch_exosims_data
from .key_map import KEY_MAP
from .logger import logger
from .plots.comparison_plots import compare, multi, panel, xy_grid
from .plots.generic_plot import extend_matplotlib, subplots
from .util import calculate_axis_limits_and_ticks, get_nice_number

# Automatically extend matplotlib with our custom methods
extend_matplotlib()

with importlib.resources.path("yieldplotlib", "style") as path:
    ypl_stylesheets = plt.style.core.read_style_directory(path)
    plt.style.core.update_nested_dict(plt.style.library, ypl_stylesheets)
    # Set the default style to ypl_default
    plt.style.use("yieldplotlib")
