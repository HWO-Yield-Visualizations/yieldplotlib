"""Data management utilities for yieldplotlib.

This module provides utilities for managing and accessing data files used by
yieldplotlib. It uses pooch to handle data downloads and caching.
"""

import pooch
from pooch import Unzip

from .load.ayo_directory import AYODirectory
from .load.exosims_directory import EXOSIMSDirectory
from .load.yip_directory import YIPDirectory

# Create a pooch registry for data files
REGISTRY = {
    "ayo.zip": "md5:af4a8853e77a19c7fe91bffb3f57ccfe",
    "exosims.zip": "md5:0ada773ec50d1bcc12c112025b8319df",
    "yip.zip": "",
}

# Create a pooch instance named after Corey's dog
PIKACHU = pooch.create(
    path=pooch.os_cache("yieldplotlib"),
    base_url="https://github.com/HWO-Yield-Visualizations/yieldplotlib/raw/main/data/",
    registry=REGISTRY,
)


def fetch_ayo_data():
    """Fetch and unpack AYO data."""
    PIKACHU.fetch("ayo.zip", processor=Unzip())
    return AYODirectory(PIKACHU.abspath / "ayo.zip.unzip/ayo")


def fetch_exosims_data():
    """Fetch and unpack EXOSIMS data."""
    PIKACHU.fetch("exosims.zip", processor=Unzip())
    return EXOSIMSDirectory(PIKACHU.abspath / "exosims.zip.unzip/exosims")


def fetch_yip_data():
    """Fetch and unpack YIP data."""
    PIKACHU.fetch("yip.zip", processor=Unzip())
    return YIPDirectory(PIKACHU.abspath / "yip.zip.unzip/yip")
