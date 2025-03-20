import yieldplotlib as ypl
import matplotlib.pyplot as plt


def ypl_pipeline(runs):
    ypl.multi(
        runs,
        x="star_dist",
        y="star_L",
        plot_type="scatter",
        c="star_comp_det",
        figsize=None,
        suptitle=None,
        layout=None,
        sharex=True,
        sharey=True,
        titles=["EXOSIMS", "AYO"],
    )
    plt.show()
