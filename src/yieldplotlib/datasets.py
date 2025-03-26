"""Data management utilities for yieldplotlib.

This module provides utilities for managing and accessing data files used by
yieldplotlib. It uses pooch to handle data downloads and caching.
"""

import pooch
from pooch import Unzip

from ._version import version

# Create a pooch registry for data files
REGISTRY = {
    "ayo.zip": "md5:af4a8853e77a19c7fe91bffb3f57ccfe",
    "exosims.zip": "md5:b3610bf81f6630ac1183f6ed9fa0dae5",
}

# Create a pooch instance named after Corey's dog
PIKACHU = pooch.create(
    path=pooch.os_cache("yieldplotlib"),
    base_url="https://github.com/HWO-Yield-Visualizations/yieldplotlib/raw/{version}/data/",
    version=version,
    registry=REGISTRY,
)


def fetch_sample_data():
    """Fetch and unpack all sample data files."""
    # Fetch and unpack AYO data
    PIKACHU.fetch("ayo.zip", processor=Unzip())

    # Fetch and unpack EXOSIMS data
    PIKACHU.fetch("exosims.zip", processor=Unzip())
