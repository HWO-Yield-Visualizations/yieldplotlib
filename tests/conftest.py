"""Test configuration for yieldplotlib."""

import pytest

from yieldplotlib.datasets import fetch_ayo_data, fetch_exosims_data


@pytest.fixture(scope="session")
def ayo_data():
    """Fixture that provides AYO data for tests.

    Returns:
        AYODirectory: An AYODirectory instance.
    """
    return fetch_ayo_data()


@pytest.fixture(scope="session")
def exosims_data():
    """Fixture that provides EXOSIMS data for tests.

    Returns:
        EXOSIMSDirectory: An EXOSIMSDirectory instance.
    """
    return fetch_exosims_data()
