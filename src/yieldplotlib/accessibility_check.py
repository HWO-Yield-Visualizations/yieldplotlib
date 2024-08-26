import numpy as np
from yieldplotlib.logger import logger
from colorspacious import cspace_converter
from yieldplotlib.util import is_monotonic


class AccessibilityChecker:
    def __init__(self, plot):
        self.plot = plot
        self.warnings = []

    def run_checks(self):
        self.check_colors()
        self.check_fonts()

        if not self.warnings:
            logger.info("All accessibility checks have passed!")

        else:
            logger.warning("Accessibility checks failed.")

    def check_colors(self):
        # Convert RGB colors into greyscale to check lightness.

        rgb = self.plot.ax.get_cmap().colors
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        lightness = lab[:, 0]

        # If there is only one color, return.
        if len(lightness) == 1:
            return

        if (np.max(lightness) - np.min(lightness)) < 50:
            warning = "Colormap does not have enough dynamic range"
            self.warnings.append(warning)
            logger.warning(warning)

        if not is_monotonic(lightness):
            warning = "Colormap is not monotonic"
            self.warnings.append(warning)
            logger.warning(warning)

    def check_fonts(self):
        return None
