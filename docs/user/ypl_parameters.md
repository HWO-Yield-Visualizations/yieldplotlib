# Common Parameters

This document provides a comprehensive list of all parameters common to both
AYO and EXOSIMS objects in `yieldplotlib`.

## Using the Parameters

Parameters can be used in various `yieldplotlib` functions to extract or plot
specific data from your simulation results:

```python
import matplotlib.pyplot as plt
from yieldplotlib.load import EXOSIMSDirectory

# Load your simulation data
exosims = EXOSIMSDirectory('path/to/exosims/run')

# Get the single visit detection completeness
det_info = exosims.get('blind_comp_det')

# Create a scatter plot of star distance vs. yield
fig, ax = plt.subplots()
ax.ypl_scatter(exosims, x='star_dist', y='yield_earth')
```

## Parameter Reference Table

The following table lists all available common parameters in yieldplotlib. This
table is regenerated on a daily basis to check for changes.

<!-- The parameter table below is auto-generated. Do not edit it directly. -->
<!-- Instead, update the Google Sheet and regenerate this documentation. -->

```{include} parameters_table.md
```
