"""Node for handling AYO's CSV files."""

import numpy as np

from yieldplotlib.core import CSVFile


class AYOCSVFile(CSVFile):
    """Node for handling reduced AYO CSV files."""

    # Mapping of keys to specific filenames
    KEY_FILENAME_MAP = {
        # Regex to match filenames ending with "-observations.csv"
        "star_name": r".*-target_list\.csv",
        "star_L": r".*-target_list\.csv",
        "star_dist": r".*-target_list\.csv",
        "star_comp": r".*-target_list\.csv",
    }

    def transform_star_name(self, data):
        """Add a prefix to the star_name data."""
        return np.array(["HIP " + str(int(name)) for name in data.values])
