"""Script to test AYO and EXOSIMS loading."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch


def plot_hist(
    temps, planet_bins, runs, run_labels, ax=None, ax_kwargs={}, use_cyberpunk=False
):
    """Plot a histogram of planet populations for different temperature bins.

    Args:
        temps (list):
            List of temperature bins to plot, e.g., ["hot", "warm", "cold"].
        planet_bins (list):
            List of planet types to plot, e.g., ["Earth", "Rocky", "Super Earth"].
        runs (list):
            List of EXOSIMSDirectories and AYODirectories to plot.
        run_labels (list):
            List of labels for each run.
        ax (matplotlib.axes.Axes, optional):
            Axes to plot on. If None, a new figure is created.
        ax_kwargs (dict, optional):
            Keyword arguments to pass to ax.set().
        use_cyberpunk (bool, optional):
            Whether to use the mplcyberpunk style. Default is False.

    Returns:
        matplotlib.figure.Figure, matplotlib.axes.Axes:
            Figure and axes objects for the plot.
    """
    if use_cyberpunk:
        import mplcyberpunk  # noqa: F401

        plt.style.use("cyberpunk")
    # Create a list of keys for the planet populations
    planet_populations = []
    for temp in temps:
        for planet_bin in planet_bins:
            if planet_bin == "Earth":
                if "yield_earth" not in planet_populations:
                    planet_populations.append("yield_earth")
            else:
                # for run, label in zip(runs, run_labels):
                planet_populations.append(
                    f"yield_{temp}_{planet_bin.lower().replace(' ', '_')}"
                )
    data = []
    for key in planet_populations:
        parts = key.split("_")
        # Extract temperature and planet type from the key
        if key == "yield_earth":
            # Assign a unique temperature category for Earth
            temperature = "earth"
            planet_type = "Earth"
        elif parts[1].lower() in ["hot", "warm", "cold"]:
            # 'hot', 'warm', 'cold'
            temperature = parts[1].lower()
            # e.g., 'Rocky', 'Super Earth'
            planet_type = "_".join(parts[2:]).replace("_", " ").title()
        else:
            # Handle unexpected formatting
            temperature = "unknown"
            planet_type = "Unknown"

        for run, label in zip(runs, run_labels):
            # Retrieve data
            run_data = run.get(key)
            try:
                value = float(run_data)
            except (ValueError, TypeError):
                value = 0  # Assign 0 if data is missing or not a number

            # Append data
            data.append(
                {
                    "planet_type": planet_type,
                    "temperature": temperature,
                    "model": label,
                    "value": value,
                }
            )

    # Create DataFrame from the data
    df = pd.DataFrame(data)

    # Define unique planet types and temperatures
    # Ensure 'Earth' is the first planet type
    plotting_earths = "yield_earth" in planet_populations
    planet_bins = ["Rocky", "Super Earth", "Sub Neptune", "Neptune", "Jupiter"]
    planet_types = [x for x in planet_bins if x in df["planet_type"].unique()]
    group_labels = ["Earth"] + planet_types if plotting_earths else planet_types
    temps = df.temperature.unique()
    # Sort to make sure it's always "hot", "warm", "cold"
    temp_order = ["hot", "warm", "cold"]
    temperatures = [x for x in temp_order if x in temps]
    df["planet_type"] = pd.Categorical(
        df["planet_type"], categories=group_labels, ordered=True
    )
    df["temperature"] = pd.Categorical(
        df["temperature"], categories=temperatures, ordered=True
    )
    df = df.sort_values(["planet_type", "temperature", "model"]).reset_index(drop=True)

    # Define color mapping for temperatures
    if not use_cyberpunk:
        color_map = {
            "earth": "#228B22",
            "hot": "#FF6347",
            "warm": "#FFD700",
            "cold": "#1E90FF",
        }
    else:
        color_map = {
            "earth": "C3",
            "hot": "C1",
            "warm": "C2",
            "cold": "C0",
        }

    # Define hatching patterns for models (runs)
    hatch_patterns = ["", "///", "\\\\", "xx", "++", "..", "**"]
    hatch_map = {}
    for i, label in enumerate(run_labels):
        hatch_map[label] = hatch_patterns[i % len(hatch_patterns)]

    # Set up the plot
    if ax is None:
        fig, ax = plt.subplots(figsize=(15, 7.5))
    else:
        fig = ax.get_figure()

    n_planets = len(planet_types)
    n_temps = len(temperatures)
    n_runs = len(runs)

    # Width of each bar
    bar_width = 0.3
    # Get the width of the earth group and the total width of the other groups
    earth_group_width = bar_width * n_runs
    temp_group_width = bar_width * n_runs * n_temps
    gap_width = bar_width / 2

    # Positions of planet groups on the x-axis
    planet_x = np.arange(
        0, (temp_group_width + gap_width) * n_planets, temp_group_width + gap_width
    )
    if plotting_earths:
        earth_group_offset = earth_group_width / 2 + gap_width + temp_group_width / 2
        planet_x += earth_group_offset

    # Iterate over each temperature and model to plot bars
    # Plot the Earth bars first
    if plotting_earths:
        for j, (run, label) in enumerate(zip(runs, run_labels)):
            offset = (j - (n_runs - 1) / 2) * bar_width
            # Filter the df to get the earth values for this run
            subset = df[(df["planet_type"] == "Earth") & (df["model"] == label)]
            _bar = ax.bar(
                offset,
                subset.value.values,
                bar_width,
                color=color_map.get("earth"),
                hatch=hatch_map.get(label),
                edgecolor="black",
                linewidth=1,
                alpha=0.8,
            )
            autolabel(ax, _bar, use_cyberpunk)

    for i, temp in enumerate(temperatures):
        for j, (run, label) in enumerate(zip(runs, run_labels)):
            # Calculate the offset for each bar
            offset = (i * n_runs + j + 0.5) * bar_width - (temp_group_width / 2)
            # Filter the DataFrame for the current temperature and model
            subset = df[(df["temperature"] == temp) & (df["model"] == label)]
            # Plot the bars
            _bar = ax.bar(
                planet_x + offset,
                subset.value.values,
                bar_width,
                color=color_map.get(temp.lower()),
                hatch=hatch_map.get(label),
                edgecolor="black",
                linewidth=1,
                alpha=0.8,
            )
            autolabel(ax, _bar, use_cyberpunk)

    # Create custom legends
    if plotting_earths:
        temp_patches = [Patch(facecolor=color_map["earth"], label="Earth")] + [
            Patch(facecolor=color_map[temp.lower()], label=temp.title())
            for temp in temperatures
        ]
    else:
        temp_patches = [
            Patch(facecolor=color_map[temp.lower()], label=temp.title())
            for temp in temperatures
        ]

    # Legend for models
    model_patches = [
        Patch(facecolor="grey", hatch=hatch_map[label], label=label)
        for label in run_labels
    ]
    # Define titles for each group
    temp_title = "Planet Type"
    model_title = "Run"

    # Combine handles and labels with titles
    handles = [Patch(alpha=0)] + temp_patches + [Patch(alpha=0)] + model_patches
    labels = (
        [temp_title]
        + [p.get_label() for p in temp_patches]
        + [model_title]
        + [p.get_label() for p in model_patches]
    )

    # Create the combined legend
    combined_legend = ax.legend(handles=handles, labels=labels, ncol=1)
    ax.add_artist(combined_legend)

    # Set labels and title
    ax.set_ylabel("Yield")
    ax.set_xticks([0] + planet_x.tolist() if plotting_earths else planet_x.tolist())
    xtick_labels = ["Earth"] + planet_types if plotting_earths else planet_types
    ax.set_xticklabels(xtick_labels, ha="center")

    ax.set(**ax_kwargs)

    return fig, ax


# Function to attach a text label above each bar displaying its height
def autolabel(ax, rects, use_cyberpunk=False):
    """Attach a text label above each bar displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.annotate(
                f"{height:.1f}",
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8,
                color="white" if use_cyberpunk else "black",
            )
