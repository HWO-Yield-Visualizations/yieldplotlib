import numpy as np
from yieldplotlib.logger import logger
from colorspacious import cspace_converter
from yieldplotlib.util import is_monotonic, rgetattr
from matplotlib.colors import to_rgb


class AccessibilityManager:
    def __init__(self, plot):
        """Manages accessibility features for a given Plot.

        Main feature is the run_checks function which will run a series of accessibility checks.
        If a check is failed it will send a warning to the console, but will not raise an error.

        Args:
            plot: yieldplotlib.core.plot.Plot
        """
        self.plot = plot
        self.warnings = []

    def run_checks(self):
        """Run accessibility checks."""
        self.check_colors()
        self.check_fonts()
        self.check_alt_text()

        if not self.warnings:
            logger.info("All accessibility checks have passed!")

        else:
            logger.warning("Accessibility checks failed.")

    def check_colors(self):
        """Checks if colors used are monotonic and span an acceptable lightness range."""
        # Convert RGB colors into greyscale to check lightness.
        rgb = []

        # If cmap is defined, get those colors.
        try:
            rgb.append(self.plot.ax.get_cmap().colors)
        except AttributeError:
            pass

        # Get colors for all lines on the axes.
        rgb.append([to_rgb(line.get_color()) for line in self.plot.ax.get_lines()])

        # Get colors for all faces (i.e. scatter points).
        rgb.append([to_rgb(s.get_facecolor()) for s in self.plot.ax.collections])
        rgb = [el for el in rgb if el !=[]][0]
        # Convert to greyscale to determine lightness.
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        lightness = lab[:, 0]

        # If there is only one color, return.
        if len(lightness) == 1:
            return

        if np.abs(np.max(lightness) - np.min(lightness)) < 50:
            warning = "Colors do not have enough dynamic range"
            self.warnings.append(warning)
            logger.warning(warning)

        if not is_monotonic(lightness):
            warning = "Colors are not monotonic"
            self.warnings.append(warning)
            logger.warning(warning)

    def check_fonts(self, size_threshold=10):
        """Checks that all font sizes in the plot are larger than a given threshold"""
        font_sizes = {}
        # Fonts to check.
        attrs = ["xaxis.label", "yaxis.label", "title", "get_xticklabels()", "get_yticklabels()"]

        for at in attrs:
            objs = rgetattr(self.plot.ax, at)
            for o in objs:
                font_sizes[at] = o.get_size()

        # Get all fonts and sizes that are less than the specified size point threshold.
        noncompliant_dict = {k: v for k, v in font_sizes.items() if v < size_threshold}

        if bool(noncompliant_dict):
            warning = (f"The following font sizes are likely too small and could present "
                       f"readability issues {noncompliant_dict}")
            self.warnings.append(warning)
            logger.warning(warning)

    def check_alt_text(self):
        """Checks if alt text has been provided for the plot."""
        if not self.plot.alt_text:
            warning = "Alt text has not been provided for this plot."
            self.warnings.append(warning)
            logger.warning(warning)

    def update_alt_text(self, alt_text):
        """Updates the alt text for the plot"""
        # Add string formatting magic if needed.
        self.plot._alt_text = alt_text