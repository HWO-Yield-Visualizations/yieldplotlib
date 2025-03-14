"""Example script demonstrating the yieldplotlib generic plotting functionality.

This example shows how to use the extended matplotlib methods to easily create plots
directly from DirectoryNode objects using key-based access.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from yieldplotlib.load import AYODirectory, EXOSIMSDirectory

EXOSIMS_DIR = Path("input/EXOSIMS/Luvoir_b_avc1_H6C_CO_DulzE_baseA")
AYO_DIR = Path("input/AYO/example")

# Load the directories
exosims = EXOSIMSDirectory(EXOSIMS_DIR)
ayo = AYODirectory(AYO_DIR)

fig, (e_ax, a_ax) = plt.subplots(ncols=2, figsize=(12, 5))

# Plot star distance vs luminosity colored by HZ completeness
e_ax.ypl_scatter(
    exosims,
    "star_dist",
    "star_L",
    c="star_comp_det",
    s=10,
    cmap="viridis",
    alpha=0.8,
)
e_ax.set_title("EXOSIMS Stars")
# Testing random things
e_ax.axhline(y=1.5, color="k", linestyle="--", alpha=0.5)
e_ax.set_xlabel("Star Distance (pc)")
e_ax.set_ylabel("Star Luminosity (L☉)")

# Same plot for AYO data
scat = a_ax.ypl_scatter(
    ayo,
    x="star_dist",
    y="star_L",
    c="star_comp_det",
    s=10,
    alpha=0.8,
)
a_ax.set_title("AYO Stars")
# Create a colorbar for the scatter plot
cbar = plt.colorbar(scat, ax=a_ax)
cbar.set_label("HZ Completeness")

fig.suptitle("Star Distribution with HZ Completeness", fontsize=16)
plt.tight_layout()
plt.savefig("star_distribution.png", dpi=300)
plt.close()

# Histogram using ypl_hist
fig, ax = plt.subplots(figsize=(8, 6))

# Create a comparative histogram of star distances
ax.ypl_hist(exosims, x="star_dist", bins=20, alpha=0.7, label="EXOSIMS Stars")
ax.ypl_hist(ayo, x="star_dist", bins=20, alpha=0.7, label="AYO Stars")

ax.set_title("Distribution of Star Distances")
ax.legend()
plt.tight_layout()
plt.savefig("star_distance_distribution.png", dpi=300)
