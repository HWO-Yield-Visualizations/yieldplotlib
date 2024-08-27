"""Script to test the EXOSIMS directory loader."""

from pathlib import Path

from yieldplotlib.load.exosims_directory import EXOSIMSDirectory

test = EXOSIMSDirectory(Path("../input/EXOSIMS/Luvoir_b_avc1_H6C_CO_DulzE_baseA/"))
print(test.display_tree())
csv_col = "chars_earth_unique"
csv_col_val = test.get(csv_col)
print(f"Column {csv_col} has values: {csv_col_val}")

# DRM test
drm_str = "det_time"
drm_val = test.get(drm_str)
print(f"DRM key {drm_str} has values: \n{drm_val}")
breakpoint()
