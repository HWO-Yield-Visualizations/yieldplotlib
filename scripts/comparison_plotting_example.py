"""Example script demonstrating the yieldplotlib comparison plotting functionality.

This example shows how to use the compare, multi, panel, and xy_grid functions to create
plots comparing multiple directory nodes. It demonstrates various ways to visualize and
compare data across different mission designs and astrophysical parameters.

Note: The input directories are hardcoded in the example script and are not
provided in the repository.
"""

from pathlib import Path

import matplotlib.pyplot as plt

import yieldplotlib as ypl
from yieldplotlib.load import AYODirectory, EXOSIMSDirectory

# Define paths to multiple directories to compare
EXOSIMS_DIRS = [
    Path("input/EXOSIMS/Luvoir_b_avc1_H6C_CO_DulzE_baseA"),
    Path("input/EXOSIMS/Luvoir_b_avc1_H6C_CO_DulzE_baseA_3ez_0ppf"),
    Path("input/EXOSIMS/Luvoir_b_avc1_H6C_CO_Dulz_baseA_3ez_0ppf"),
]
exosims_labels = [
    "LUVOIR-B Base",
    "LUVOIR-B 3ez Earths",
    "LUVOIR-B 3ez",
]

AYO_DIRS = [
    Path("input/AYO/example"),
]

# Load all the directories
exosims_runs = [EXOSIMSDirectory(path) for path in EXOSIMS_DIRS]
ayo_runs = [AYODirectory(path) for path in AYO_DIRS]

all_runs = exosims_runs + ayo_runs

# Example 1: Simple comparison on a single axes with color key
fig, ax = plt.subplots(figsize=(10, 6))

# Compare multiple EXOSIMS runs on the same axes, colored by star luminosity
ypl.compare(
    ax,
    all_runs,
    x="star_dist",
    y="star_comp_det",
    plot_type="scatter",
    labels=exosims_labels,
    c="star_L",
    cmap="viridis",
    alpha=0.7,
    s=50,
)

ax.set_title("Star Properties Across Mission Designs")
ax.set_xlabel("Distance (pc)")
ax.set_ylabel("Detection completeness")
ax.grid(True, alpha=0.3)

# Add colorbar
cbar = plt.colorbar(ax.collections[0])
cbar.set_label("Star Luminosity (L☉)")

plt.tight_layout()
plt.savefig("plot1_comparison_scatter_colored.png", dpi=300)
plt.close()

# Example 2: Multi-panel figure with one subplot per directory
fig, axes = ypl.multi(
    exosims_runs,
    x="star_dist",
    y="star_L",
    plot_type="scatter",
    figsize=(15, 5),
    suptitle="Stellar Population Comparison",
    layout=(1, 3),
    titles=exosims_labels,
    c="star_comp_det",
    cmap="viridis",
    alpha=0.7,
    s=50,
)

# Add common elements to all subplots
for ax in axes.flatten():
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("Distance (pc)")
    ax.set_ylabel("Luminosity (L☉)")

# Add colorbar
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cbar = plt.colorbar(axes[0, 0].collections[0], cax=cbar_ax)
cbar.set_label("Detection completeness")

plt.savefig("plot2_multi_panel_comparison_colored.png", dpi=300)
plt.close()

# Example 3: Panel with different plot types for each column
fig, axes = ypl.panel(
    [exosims_runs[0], ayo_runs[0]],
    {
        "x": "star_dist",
        "y": "star_L",
        "plot_type": "scatter",
        "alpha": 0.7,
        "c": "star_comp_det",
        "cmap": "viridis",
        "s": 50,
    },
    {
        "x": "star_dist",
        "plot_type": "hist",
        "bins": 30,
        "alpha": 0.7,
        "c": "star_L",
        "cmap": "viridis",
    },
    figsize=(15, 8),
    suptitle="EXOSIMS vs AYO Comparison",
    layout=(2, 2),
)

# Add common styling and colorbars
for ax in axes.flatten():
    ax.grid(True, alpha=0.3)
    if ax.collections:  # If the axes has scatter plots
        cbar = plt.colorbar(ax.collections[0], ax=ax)
        if "star_comp_det" in ax.collections[0].get_array():
            cbar.set_label("Detection completeness")
        else:
            cbar.set_label("Star Luminosity (L☉)")

plt.tight_layout()
plt.savefig("plot3_complex_panel_comparison_colored.png", dpi=300)
plt.close()

# Example 4: Grid of scatter plots comparing multiple parameters
# Define the parameters we want to compare
x_keys = [
    "star_dist",  # Distance to target stars
    "exp_time_char",  # Characterization exposure time
]

y_keys = [
    "star_L",  # Stellar luminosity
    "star_comp_det",  # Stellar completeness
]

# Create the grid of plots with color keys
fig, axes = ypl.xy_grid(
    [exosims_runs[0], ayo_runs[0]],
    x_keys,
    y_keys,
    plot_type="scatter",
    figsize=(15, 15),
    suptitle="Astrophysical Parameter Relationships",
    legend=True,
    alpha=0.6,
    s=50,
    c="star_comp_det",
    cmap="viridis",
)

# Add some custom formatting to make the plots more readable
for ax in axes.flatten():
    ax.grid(True, alpha=0.3)  # Light grid for better readability
    ax.tick_params(axis="both", which="major", labelsize=8)  # Smaller font for ticks
    ax.tick_params(
        axis="both", which="minor", labelsize=6
    )  # Smaller font for minor ticks

# Add colorbar
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cbar = plt.colorbar(axes[0, 0].collections[0], cax=cbar_ax)
cbar.set_label("Detection completeness")

plt.savefig("plot4_parameter_grid_colored.png", dpi=300, bbox_inches="tight")
plt.close()

# Example 5: Grid of histogram plots for distribution analysis
fig, axes = ypl.xy_grid(
    [exosims_runs[0], ayo_runs[0]],
    ["star_dist", "exp_time_char"],
    None,
    plot_type="hist",
    figsize=(15, 5),
    suptitle="Parameter Distributions",
    legend=True,
    sharex=False,
    sharey=False,
    alpha=0.7,
    c="star_L",
    cmap="viridis",
)

# Add some custom formatting
for ax in axes.flatten():
    ax.grid(True, alpha=0.3)
    ax.tick_params(axis="both", which="major", labelsize=8)
    ax.tick_params(axis="both", which="minor", labelsize=6)


plt.savefig("plot5_parameter_distributions_colored.png", dpi=300, bbox_inches="tight")
plt.close()

print("All comparison examples saved successfully!")
