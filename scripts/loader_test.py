"""Script to test AYO and EXOSIMS loading."""

from pathlib import Path

import matplotlib.pyplot as plt
from yieldplotlib.load import AYODirectory, EXOSIMSDirectory

exosims = EXOSIMSDirectory(Path("../input/EXOSIMS/Luvoir_b_avc1_H6C_CO_DulzE_baseA/"))
ayo = AYODirectory(Path("../input/AYO/example"))
print(exosims.display_tree())
print(ayo.display_tree())

runs = [exosims, ayo]
titles = ["EXOSIMS", "AYO"]
fig, axs = plt.subplots(1, len(runs), figsize=(15, 5))
y_range = (0.001, 200)
for i, (run, title) in enumerate(zip(runs, titles)):
    star_L = run.get("star_L")
    star_dist = run.get("star_dist")
    star_comp = run.get("star_comp")
    axs[i].scatter(star_dist, star_L, c=star_comp, cmap="viridis")
    axs[i].set_xlabel("Distance [pc]")
    axs[i].set_ylabel("Luminosity [L_sun]")
    axs[i].set_ylim(y_range)
    axs[i].set_yscale("log")
    axs[i].set_title(f"{run.file_name} ({title})")
plt.show()
