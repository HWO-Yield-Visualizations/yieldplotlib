from yieldplotlib.load.exosims_directory import EXOSIMSDirectory
from yieldplotlib.load.ayo_directory import AYODirectory
from pathlib import Path
from yieldplotlib.plots.yield_hist import plot_hist
import matplotlib.pyplot as plt
from yieldplotlib.plots.hz_completeness import plot_hz_completeness
from yieldplotlib.plots.yip_plots import plot_core_throughtput
from yieldplotlib.load.yip_directory import YIPDirectory

ayo = AYODirectory(Path("/Users/ssteiger/repos/yieldplotlib/input/AYO/EAC1_yields/EAC1-QE_0.9-noiseless-H2O"))
exosims = EXOSIMSDirectory(Path("/Users/ssteiger/repos/yieldplotlib/input/EXOSIMS/Example_EAC1_EXOSIMS2_QE90_noiseless"))
yip = YIPDirectory(Path("/Users/ssteiger/repos/yieldplotlib/input/eac1_aavc"))
# temps = ["hot", "warm", "cold"]
# planet_bins = ["Earth", "Rocky", "Super Earth", "Sub Neptune", "Neptune", "Jupiter"]
# runs = [exosims]
# run_labels = ["EXOSIMS"]
# fig, ax = plot_hist(temps, planet_bins, runs, run_labels, ax=None, ax_kwargs={"ylim":(0, 75)}, use_cyberpunk=True)
# plt.title("Planet Yield Histograms", fontsize=20)
# ax.tick_params(axis='y', labelsize=16)
# plt.savefig("/Users/ssteiger/repos/yieldplotlib/paper/figures/yield_hist_cyber.png")
# plt.show()
#
# plot_hz_completeness(exosims,
#                      ayo,
#                      ax_kwargs={"yscale": "log", "ylim":(5e-3, 50), "xlim":(0.1, 20)},
#                      hline_kwargs={"linewidth": 2, "color":"white", "alpha":0.7, "zorder":0},
#                      use_cyberpunk=True)
# plt.savefig("/Users/ssteiger/repos/yieldplotlib/paper/figures/hz_completeness_cyber.png")
# plt.show()

fig, ax = plot_core_throughtput([exosims], ["EXOSIMS"], yip,
                      title="Coronagraph Throughput", use_cyberpunk=False,
                      ax_kwargs={"xlim": (0, 32),
                                 "ylim": (0, 0.4)})

plt.savefig('/Users/ssteiger/repos/yieldplotlib/paper/figures/core_throughput_all_curves.jpeg')
plt.show()