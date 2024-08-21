"""TODO."""

from pathlib import Path

import matplotlib.pyplot as plt
import yieldplotlib as ypl

# Option 1 - Do not tie plots to axes/data specifically
run_path = Path("../input/AYO/example/")
yield_result = ypl.YieldResult(run_path)

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))

plot_kwargs = {"c": yield_result.data["Visit #"]}

plot_1 = ypl.Plot(x="distance", y="yield", plot_kwargs=plot_kwargs)
plot_2 = ypl.Plot(x="distance", y="exposure_time", plot_kwargs=plot_kwargs)

axes[0] = plot_1.plot(yield_result, axes[0])
axes[1] = plot_2.plot(yield_result, axes[1])
fig.suptitle(yield_result.run_name)
plt.show()

# Option 2 - Tie plots to axes/data specifically
