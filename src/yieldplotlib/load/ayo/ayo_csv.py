"""Node for handling AYO's CSV files."""

import numpy as np
import pandas as pd

from yieldplotlib.core import CSVFile
from yieldplotlib.util import get_unit

OVERRIDE_KEYS = {
    "blind_comp_det": "_get_blind_comp",
    "Core throughput": "_get_core_thruput",
}


class AYOCSVFile(CSVFile):
    """Node for handling reduced AYO CSV files."""

    def transform_star_name(self, data):
        """Add a prefix to the star_name data."""
        return np.array(["HIP " + str(int(name)) for name in data])

    def transform_WDS_sep(self, data):
        """Convert the WDS separation to floats."""
        return np.array(data, dtype=float)

    def transform_WDS_dmag(self, data):
        """Convert the WDS dMag to floats."""
        return np.array(data, dtype=float)

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        if key in OVERRIDE_KEYS:
            return getattr(self, OVERRIDE_KEYS[key])()
        unit = get_unit(key, self.__class__.__name__)

        if key in self.data.columns:
            if unit:
                return self.data[key].values * unit
            else:
                return self.data[key].values
        return None

    def _get_blind_comp(self):
        """Get the blind completeness data from first visits.

        Returns:
            np.ndarray:
                A structured array with completeness, star names, and integration times
                for all first visits.
        """
        # Filter data to only include first visits
        first_visits = self.data[self.data["Visit #"] == 1]

        # Extract the required data
        completeness = first_visits["exoEarth candidate yield"].values.astype(float)
        hip_ids = first_visits["HIP"].values
        integration_times = first_visits["Exp Time (days)"].values.astype(float)

        # Create star names with HIP prefix
        star_names = np.array([f"HIP {int(hip)}" for hip in hip_ids])

        # Create a structured array with the data
        result = pd.DataFrame(
            {
                "completeness": completeness,
                "star_name": star_names,
                "integration_time": integration_times,
            },
        )

        return result

    def _get_core_thruput(self):
        """Get the core thruput data."""
        # Get both wavelength and core throughput
        sep = self.data["Sep (l/D)"].values
        thruput = self.data["Core throughput"].values
        df = pd.DataFrame({"sep": sep, "thruput": thruput})
        return df
