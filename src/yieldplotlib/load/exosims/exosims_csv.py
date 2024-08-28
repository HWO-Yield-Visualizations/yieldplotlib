"""Node for handling EXOSIMS-Sandbox's reduced CSV files."""

from yieldplotlib.core import CSVFile


class EXOSIMSCSVFile(CSVFile):
    """Node for handling reduced EXOSIMS CSV files."""

    # Mapping of keys to specific filenames
    KEY_FILENAME_MAP = {
        "star_name": "reduce-star-target.csv",
        "star_L": "reduce-star-target.csv",
        "star_dist": "reduce-star-target.csv",
        "star_comp": "reduce-star-target.csv",
    }

    def transform_star_name(self, data):
        """Add a prefix to the star_name data."""
        return data.values

    # def _get(self, key: str):
    #     """Custom logic for CSV files."""
    #     # TODO: Implement custom logic for CSV files.
    #     if key == "star_name":
    #         return self.data["star_name"]
    #     return super()._get(key)
    #
    # @property
    # def star_name(self):
    #     """Get the star name from the CSV file."""
    #     col = self._get("star_name")
    #     return self.get("star_name")
