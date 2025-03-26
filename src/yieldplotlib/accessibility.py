"""Accessibility features for yieldplotlib."""

import matplotlib
import numpy as np
from colorspacious import cspace_converter
from matplotlib.colors import to_rgb

from yieldplotlib.logger import logger
from yieldplotlib.util import is_monotonic, rgetattr


class AccessibilityManager:
    """Manages accessibility features for a given matplotlib.axes.Axes."""

    def __init__(self, ax):
        """Manages accessibility features for a given matplotlib.axes.Axes.

        Main feature is the run_checks function which will run a series of
        accessibility checks. If a check is failed it will send a warning to
        the console, but will not raise an error.

        Args:
            ax (matplotlib.axes.Axes):
                Axes object on which to run the accessibility checks.
        """
        self.ax = ax
        self.warnings = []

    def run_checks(self):
        """Run accessibility checks."""
        self.check_colors()
        self.check_fonts()

        if not self.warnings:
            logger.info("All accessibility checks have passed!")

        else:
            logger.warning(f"{len(self.warnings)} accessibility checks failed.")

    def check_colors(self):
        """Check if colors used are monotonic and span an acceptable lightness range."""
        # Convert RGB colors into greyscale to check lightness.
        rgb = []

        # If cmap is defined, get a sample of those colors.
        try:
            rgb_values = [
                image.cmap(np.arange(0, 1, 0.1))[:, :3] for image in self.ax.images
            ]
            for val in rgb_values[0]:
                rgb.append([val[0], val[1], val[2]])
        except IndexError:
            pass

        # Get colors for all lines on the axes.
        line_colors = [list(to_rgb(line.get_color())) for line in self.ax.get_lines()]
        for lc in line_colors:
            rgb.append(lc)

        # Get colormap used for scatter points.
        try:
            scatter_cmap = self.ax.collections[0].get_cmap()
            if isinstance(scatter_cmap, matplotlib.colors.LinearSegmentedColormap):
                rgb_values = self.ax.collections[0].get_cmap()(np.arange(0, 1, 0.1))[
                    :, :3
                ]
                cmap_colors = []
                for val in rgb_values:
                    cmap_colors.append([val[0], val[1], val[2]])

            else:
                cmap_colors = scatter_cmap.colors
                cmap_colors = [to_rgb(color) for color in cmap_colors]

            cmap_lab = cspace_converter("sRGB1", "CAM02-UCS")(cmap_colors)
            cmap_lightness = cmap_lab[:, 0]

            if not is_monotonic(cmap_lightness):
                warning = "Colormap for scatter points is not monotonic"
                self.warnings.append(warning)
                logger.warning(warning)

        except IndexError:
            pass

        # Get colors for all faces.
        fcs = [s.get_facecolor() for s in self.ax.collections]
        face_colors = [list(to_rgb(fc)) for fc in np.squeeze(fcs)]
        for fc in face_colors:
            rgb.append(fc)

        # Get colors for all containers (i.e. bars)
        container_colors = [
            list(to_rgb(b.get_facecolor())) for c in self.ax.containers for b in c
        ]
        for cc in container_colors:
            rgb.append(cc)

        # Clean up the RBG values.
        rgb = [el for el in rgb if el != []]

        # Convert to greyscale to determine lightness.
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        lightness = lab[:, 0]

        # If there is only one color, return.
        if len(lightness) == 1:
            return

        if np.abs(np.max(lightness) - np.min(lightness)) < 50:
            warning = (
                f"Colors do not have enough dynamic range, lightness "
                f"difference is"
                f" {np.abs(np.max(lightness) - np.min(lightness)):.2f} "
                f"and should be at least 50."
            )
            self.warnings.append(warning)
            logger.warning(warning)

        if not is_monotonic(lightness):
            warning = "Colors may not be monotonic"
            self.warnings.append(warning)
            logger.warning(warning)

    def check_fonts(self, size_threshold=10):
        """Checks that all font sizes in the plot are larger than a given threshold."""
        font_sizes = {}
        # Fonts to check with a get_size() property.
        attrs = [
            "xaxis.label",
            "yaxis.label",
            "title",
            "get_xticklabels",
            "get_yticklabels",
        ]

        for at in attrs:
            objs = rgetattr(self.ax, at)
            try:
                font_sizes[at] = objs.get_size()
            except AttributeError:
                eval = objs()
                for item in eval:
                    font_sizes[at] = item.get_size()

        # Get font sizes for annotations and legends.
        for child in self.ax.get_children():
            if isinstance(child, matplotlib.text.Annotation):
                font_sizes[child] = child.get_fontsize()
            if isinstance(child, matplotlib.legend.Legend):
                for leg in child.get_texts():
                    font_sizes[leg] = leg.get_fontsize()

        # Get all fonts and sizes that are less than the specified size point threshold.
        noncompliant_dict = {k: v for k, v in font_sizes.items() if v < size_threshold}

        if bool(noncompliant_dict):
            warning = (
                f"The following font sizes are likely too small and could present "
                f"readability issues {noncompliant_dict}"
            )
            self.warnings.append(warning)
            logger.warning(warning)
