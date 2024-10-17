"""yieldplotlib - A library for plotting yield data."""

__all__ = [
    "__version__",
    "KEY_MAP",
    "logger",
    "calculate_axis_limits_and_ticks",
    "get_nice_number",
]

import os
from pathlib import Path

import matplotlib.pyplot as plt

from ._version import __version__
from .key_map import KEY_MAP
from .logger import logger
from .util import calculate_axis_limits_and_ticks, get_nice_number

# Get the absolute path of the current script
current_file = Path(__file__).resolve()
# Navigate up to the repository root
repo_root = current_file.parent.parent.parent

stylelib_dir = os.path.join(repo_root, "mplstyles/ypl_default.mplstyle")
plt.style.use(stylelib_dir)
