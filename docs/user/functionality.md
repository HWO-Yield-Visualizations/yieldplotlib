# Methods and Functionality

## Parsing and Getting Values
`yieldplotlib` provides a loading system with a unified interface for accessing data from
the yield codes. The system manages the complex and inconsistent file structures of the
AYO and EXOSIMS inputs and outputs by organizing them into a hierarchical tree of nodes
representing files and directories. This abstraction creates a consistent API that
allows users to query data without needing to understand and parse the underlying
data products. For collaboration purposes, the valid queries are managed in a
[Google Sheet](https://docs.google.com/spreadsheets/d/1qZ-JH0xnYSqeWOrirEIvJ-NcoMVu90pDgeRsqbDUcxM/edit?usp=sharing) where collaborators have linked the EXOSIMS and AYO keys to a
universal key in `yieldplotlib`. This Google Sheet is processed into a `key_map` which
is updated daily. Users can view, download, and process the CSV file locally for development.
If you would like editing access to the Google Sheet, reach out via email to
Corey (corey.a.spohn@nasa.gov) or Sarah (ssteiger@stsci.edu).

Once the yield packages are loaded and parsed, a getter can be called on the directory objects
to return the corresponding value from the respective yield code, for example:

```angular2html
from yieldplotlib.load import AYODirectory, EXOSIMSDirectory

ayo = AYODirectory(Path("path/to/my/ayo_data"))
exosims = EXOSIMSDirectory(Path("path/to/my/exosims_data"))

ayo.get("yield_earth")
exosims.get("yield_earth")
```

Yield input packages (YIPs) specifying input coronagraph parameters can also be loaded and accessed
using the same file node and directory structure. This allows users to access key coronagraph performance
metrics that serve as critical inputs to these yield codes. In order to process the YIPs, `yieldplotlib`
uses [yippy](https://github.com/CoreySpohn/yippy) as a backend, though the user interface is identical to generating the AYO and EXOSIMS
directories, for example:


```angular2html
from yieldplotlib.load import YIPDirectory

yip = YIPDirectory(Path("path/to/my/yip_data"))
```

## Plotting

### Generic and Comparison Plots

`yieldplotlib` extends the commonly used Python plotting package `matplotlib` to take advantage
of the wide variety of customization options that  `matplotlib` offers. The `yieldplotlib` generic
plots are used for single yield run visualizations and can make scatter plots, standard plots,
and histograms. This extension is achieved through a function that runs when `yieldplotlib`
is imported that automatically adds new plotting methods (prefixed with `ypl_`) to `matplotlib`'s
`Axes` class, allowing users to directly call methods like `ax.ypl_plot()` and
`ax.ypl_scatter()` on any `matplotlib` axes object.

Also provided are comparison plots that can handle multiple yield runs and automatically create
multi-panel figures.

### Plotting Scripts
`yieldplotlib` contains scripts for generating common plots used in yield code visualizations to
provide instant usability for comparing AYO and EXOSIMS as motivated by the rapid pace of the ongoing
architecture trade studies for HWO. This also serves to provide examples on how the package can be
used for those who want to adapt the generic `yieldplotlib` parsing structure and plotting methods to
generate their own bespoke visualizations.


## Pipeline and Command Line Interface

In order to generate summary plots quickly, `yieldplotlib` comes packaged with a command line interface
and plotting pipeline to create a suite of commonly used yield plots. This is accessed through the terminal
by:

```angular2html
ypl_run path/to/yield/runs
```
where the specified path is either to a single folder containing the outputs for a single AYO or EXOSIMS run,
or to a directory containing subdirectories of many AYO and EXOSIMS runs.
