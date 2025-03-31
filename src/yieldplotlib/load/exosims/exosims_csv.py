"""Node for handling EXOSIMS-Sandbox's reduced CSV files."""

from yieldplotlib.core import CSVFile
from yieldplotlib.util import get_unit


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

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        unit = get_unit(key, self.__class__.__name__)

        if key in self.data.columns:
            if unit:
                return self.data[key].values * unit
            else:
                return self.data[key].values
        return None
