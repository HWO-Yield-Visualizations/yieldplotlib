"""Node for handling EXOSIMS-Sandbox's reduced CSV files."""

from yieldplotlib.core import CSVFile


class EXOSIMSCSVFile(CSVFile):
    """Node for handling reduced EXOSIMS CSV files."""

    def transform_yield_hot_rocky(self, data):
        """Return the yield of Earth-like planets."""
        return data

    def transform_yield_warm_rocky(self, data):
        """Return the yield of Earth-like planets."""
        return data.values

    def transform_yield_cold_rocky(self, data):
        """Return the yield of Earth-like planets."""
        return data.values
