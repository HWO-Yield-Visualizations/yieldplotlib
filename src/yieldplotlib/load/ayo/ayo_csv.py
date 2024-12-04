"""Node for handling AYO's CSV files."""

import numpy as np

from yieldplotlib.core import CSVFile


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
