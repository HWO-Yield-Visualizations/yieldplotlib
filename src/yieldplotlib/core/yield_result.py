"""TODO."""

from pathlib import Path

import pandas as pd

from yieldplotlib.logger import logger


class YieldResult:
    """TODO."""

    def __init__(self, run_path):
        """TODO."""
        self.run_path = run_path
        self.data = self.load_data()

    def load_data(self):
        """TODO."""
        csv_file = self.find_csv_file(self.run_path)
        if csv_file:
            data = pd.read_csv(csv_file)
            # Rename columns (stub)
            data = self.rename_columns(data)
            return data
        else:
            raise FileNotFoundError(f"No CSV file found in {self.run_path}")

    def find_csv_file(self, path):
        """Find the first CSV file ending with 'observations.csv' in the directory."""
        path = Path(path)
        for file_path in path.glob("*.csv"):
            # Iterate through all CSV files in the directory
            if file_path.name.endswith("observations.csv"):
                logger.debug(f"Found CSV file: {file_path.name}")
                self.run_name = file_path.name
                return file_path
        return None

    def rename_columns(self, data):
        """TODO."""
        # Placeholder for column renaming logic
        replace_dict = {
            "dist (pc)": "distance",
            "exoEarth candidate yield": "yield",
            "Exp Time (days)": "exposure_time",
        }
        for old_name, new_name in replace_dict.items():
            if old_name in data.columns:
                data.rename(columns={old_name: new_name}, inplace=True)
        logger.debug(f"Renamed column {old_name} to {new_name}")
        return data
