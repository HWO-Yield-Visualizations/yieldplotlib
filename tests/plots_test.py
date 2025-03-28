"""Tests for the plotting functionality."""

import matplotlib.pyplot as plt
import pytest

from yieldplotlib.plots import compare, multi, panel, plot_hist, xy_grid


def test_plot_hist(ayo_data, exosims_data):
    """Test that the histogram plotting functionality works without errors."""
    try:
        plot_hist(
            temps=["hot", "warm", "cold"],
            planet_bins=["Rocky", "Super Earth", "Sub Neptune", "Neptune", "Jupiter"],
            runs=[ayo_data, exosims_data],
            run_labels=["AYO", "EXOSIMS"],
            use_cyberpunk=True,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"plot_hist failed with error: {str(e)}")


@pytest.mark.parametrize("plot_type", ["scatter", "plot", "hist"])
def test_compare_plot_types(ayo_data, exosims_data, plot_type):
    """Test comparison with different plot types."""
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        kwargs = {
            "ax": ax,
            "directories": [ayo_data, exosims_data],
            "x": "star_dist",
            "plot_type": plot_type,
            "labels": ["AYO", "EXOSIMS"],
            "alpha": 0.7,
        }

        # Add y parameter for non-histogram plots
        if plot_type != "hist":
            kwargs["y"] = "star_L"

        # Add plot-specific parameters
        if plot_type == "scatter":
            kwargs.update({"c": "star_L", "cmap": "viridis", "s": 50})
        elif plot_type == "plot":
            kwargs["linestyles"] = ["-", "--"]
        elif plot_type == "hist":
            kwargs["bins"] = 20

        compare(**kwargs)
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"compare {plot_type} plot failed with error: {str(e)}")


def test_compare_custom_style(ayo_data, exosims_data):
    """Test comparison with custom markers and colors."""
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        compare(
            ax,
            [ayo_data, exosims_data],
            x="star_dist",
            y="star_L",
            plot_type="scatter",
            labels=["AYO", "EXOSIMS"],
            markers=["o", "s"],
            colors=["red", "blue"],
            alpha=0.7,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"compare custom style failed with error: {str(e)}")


def test_compare_no_legend(ayo_data, exosims_data):
    """Test comparison without legend."""
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        compare(
            ax,
            [ayo_data, exosims_data],
            x="star_dist",
            y="star_L",
            plot_type="scatter",
            labels=["AYO", "EXOSIMS"],
            legend=False,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"compare no legend failed with error: {str(e)}")


@pytest.mark.parametrize("plot_type", ["scatter", "plot", "hist"])
def test_multi_plot_types(ayo_data, exosims_data, plot_type):
    """Test multi-panel with different plot types."""
    try:
        kwargs = {
            "directories": [ayo_data, exosims_data],
            "x": "star_dist",
            "plot_type": plot_type,
            "figsize": (12, 5),
            "suptitle": f"Multi-panel {plot_type} plot",
            "layout": (1, 2),
            "titles": ["AYO", "EXOSIMS"],
            "alpha": 0.7,
        }

        # Add y parameter for non-histogram plots
        if plot_type != "hist":
            kwargs["y"] = "star_L"

        # Add plot-specific parameters
        if plot_type == "scatter":
            kwargs.update({"c": "star_comp_det", "cmap": "viridis"})
        elif plot_type == "plot":
            kwargs["linestyles"] = ["-", "--"]
        elif plot_type == "hist":
            kwargs["bins"] = 20

        fig, axes = multi(**kwargs)
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"multi {plot_type} plot failed with error: {str(e)}")


def test_multi_auto_layout(ayo_data, exosims_data):
    """Test multi-panel with auto layout."""
    try:
        fig, axes = multi(
            [ayo_data, exosims_data],
            x="star_dist",
            y="star_L",
            plot_type="scatter",
            figsize=(12, 5),
            suptitle="Auto Layout Test",
            titles=["AYO", "EXOSIMS"],
            alpha=0.7,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"multi auto layout failed with error: {str(e)}")


def test_multi_shared_axes(ayo_data, exosims_data):
    """Test multi-panel with shared axes."""
    try:
        fig, axes = multi(
            [ayo_data, exosims_data],
            x="star_dist",
            y="star_L",
            plot_type="scatter",
            figsize=(12, 5),
            suptitle="Mixed Plot Types",
            layout=(1, 2),
            titles=["AYO", "EXOSIMS"],
            sharex=True,
            sharey=True,
            alpha=0.7,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"multi shared axes failed with error: {str(e)}")


def test_multi_custom_style(ayo_data, exosims_data):
    """Test multi-panel with custom styling."""
    try:
        fig, axes = multi(
            [ayo_data, exosims_data],
            x="star_dist",
            y="star_L",
            plot_type="scatter",
            figsize=(12, 5),
            suptitle="Custom Styling",
            layout=(1, 2),
            titles=["AYO", "EXOSIMS"],
            markers=["o", "s"],
            colors=["red", "blue"],
            alpha=0.7,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"multi custom style failed with error: {str(e)}")


@pytest.mark.parametrize("plot_type", ["scatter", "plot", "hist"])
def test_panel_plot_types(ayo_data, exosims_data, plot_type):
    """Test panel with different plot types."""
    try:
        kwargs = {
            "figsize": (10, 8),
            "suptitle": f"Panel {plot_type} plot",
            "layout": (2, 1),
        }

        # Create spec based on plot type
        spec = {"x": "star_dist", "plot_type": plot_type, "alpha": 0.7}
        if plot_type != "hist":
            spec["y"] = "star_L"

        # Add plot-specific parameters
        if plot_type == "scatter":
            spec.update({"c": "star_comp_det", "cmap": "viridis"})
        elif plot_type == "plot":
            spec["linestyle"] = "--"
        elif plot_type == "hist":
            spec["bins"] = 20

        fig, axes = panel([ayo_data, exosims_data], spec, **kwargs)
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"panel {plot_type} plot failed with error: {str(e)}")


def test_panel_mixed_types(ayo_data, exosims_data):
    """Test panel with mixed plot types."""
    try:
        fig, axes = panel(
            [ayo_data, exosims_data],
            {
                "x": "star_dist",
                "y": "star_L",
                "plot_type": "scatter",
                "alpha": 0.7,
                "c": "star_comp_det",
                "cmap": "viridis",
            },
            {
                "x": "star_dist",
                "y": "star_comp_det",
                "plot_type": "plot",
                "alpha": 0.7,
                "linestyle": "--",
            },
            figsize=(12, 5),
            suptitle="Mixed Plot Types",
            layout=(1, 2),
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"panel mixed types failed with error: {str(e)}")


def test_panel_custom_titles(ayo_data, exosims_data):
    """Test panel with custom titles."""
    try:
        fig, axes = panel(
            [ayo_data, exosims_data],
            {
                "x": "star_dist",
                "y": "star_L",
                "plot_type": "scatter",
                "alpha": 0.7,
            },
            {
                "x": "star_dist",
                "plot_type": "hist",
                "bins": 20,
                "alpha": 0.7,
            },
            figsize=(10, 8),
            suptitle="Custom Titles",
            titles=["Distance vs Luminosity", "Distance Distribution"],
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"panel custom titles failed with error: {str(e)}")


def test_panel_shared_axes(ayo_data, exosims_data):
    """Test panel with shared axes."""
    try:
        fig, axes = panel(
            [ayo_data, exosims_data],
            {
                "x": "star_dist",
                "y": "star_L",
                "plot_type": "scatter",
                "alpha": 0.7,
            },
            {
                "x": "star_dist",
                "plot_type": "hist",
                "bins": 20,
                "alpha": 0.7,
            },
            figsize=(10, 8),
            suptitle="Shared Axes",
            layout=(2, 1),
            sharex=True,
            sharey=False,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"panel shared axes failed with error: {str(e)}")


@pytest.mark.parametrize("plot_type", ["scatter", "plot", "hist"])
def test_xy_grid_plot_types(ayo_data, exosims_data, plot_type):
    """Test xy grid with different plot types."""
    try:
        kwargs = {
            "directories": [ayo_data, exosims_data],
            "plot_type": plot_type,
            "figsize": (10, 10),
            "suptitle": f"XY Grid {plot_type} plot",
            "legend": True,
            "alpha": 0.6,
        }

        if plot_type == "hist":
            kwargs.update(
                {
                    "x_keys": ["star_dist", "exp_time_char"],
                    "y_keys": None,
                    "bins": 20,
                }
            )
        else:
            kwargs.update(
                {
                    "x_keys": ["star_dist", "exp_time_char"],
                    "y_keys": ["star_L", "star_comp_det"],
                }
            )

        if plot_type == "scatter":
            kwargs.update({"c": "star_comp_det", "cmap": "viridis"})

        fig, axes = xy_grid(**kwargs)
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"xy grid {plot_type} plot failed with error: {str(e)}")


def test_xy_grid_custom_style(ayo_data, exosims_data):
    """Test xy grid with custom styling."""
    try:
        fig, axes = xy_grid(
            [ayo_data, exosims_data],
            ["star_dist"],
            ["star_L", "star_comp_det"],
            plot_type="scatter",
            figsize=(5, 10),
            suptitle="Custom Styling",
            legend=True,
            markers=["o", "s"],
            colors=["red", "blue"],
            alpha=0.7,
        )
        plt.close()
    except Exception as e:
        plt.close()
        pytest.fail(f"xy grid custom style failed with error: {str(e)}")


if __name__ == "__main__":
    import yieldplotlib as ypl

    exosims_data = ypl.fetch_exosims_data()
    ayo_data = ypl.fetch_ayo_data()
    test_panel_plot_types(ayo_data, exosims_data, "scatter")
