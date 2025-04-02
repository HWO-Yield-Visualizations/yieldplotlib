---
title: "yieldplotlib: A unified library for exoplanet yield code visualizations"
tags:
  - Python
  - astronomy
  - exoplanets
  - yields
  - visualizations
authors:
  - name: Corey Spohn
    orcid: 0000-0002-3138-0240
    equal-contrib: true
    affiliation: "1"

  - name: Sarah Steiger
    orcid: 0000-0002-4787-3285
    equal-contrib: true
    affiliation: "2"

  - name: Alex R. Howe
    orcid: 0000-0002-4884-7150
    equal-contrib: false
    affiliation: "1, 3, 4"

affiliations:
  - name: Goddard Space Flight Center, United States
    index: 1
  - name: Space Telescope Science Institute, United States
    index: 2
  - name: The Catholic University of America, United States
    index: 3
  - name: Center for Research and Exploration in Space Science and Technology, NASA/GSFC, United States
    index: 4

date: 1 April 2025
bibliography: paper.bib
---

# Summary

NASA’s next flagship observatory, the Habitable Worlds Observatory (HWO), aims
to detect and charaterize ~25 habitable zone planets. The total number of
habitable zone planets detected is referred to as the exo-Earth "yield" and
accurate yield estimates will be critically important to the mission's success. Tools
like the Altruistic Yield Optimizer (AYO) and EXOSIMS provide these yield
estimates but differ in language, methods, and outputs. `yieldplotlib` provides
a unified library that can visualize the inputs and outputs of these yield
codes in a complete, descriptive, and accessible way.

# Statement of need

To evaluate different designs for HWO [@HWOFeinberg2024], yield codes such as AYO [@AYO2014] and EXOSIMS
[@EXOSIMS2016] calculate the expected exo-Earth yield for each architecture.
While these yield codes have the same goal, their implementations
are so different that validation has become a major obstacle for the community.

Previous cross-calibration efforts have already provided valuable insights. @ETCCrossCal2025 compared
the internal exposure time calculations of AYO and EXOSIMS and revealed previously unknown
discrepancies. `yieldplotlib` is a more ambitious continuation of that work.
It is a Python library capable of easily accessing hundreds of important quantities
from both AYO and EXOSIMS.

To visualize the inputs and outputs of AYO and EXOSIMS, `yieldplotlib` uses a custom loading and
parsing structure to easily access equivalent data across both codes.
This allows `yieldplotlib` to communicate the results of yield codes to the broader community
and produce publication-quality plots without manually processing the complex underlying data.
Currently `yieldplotlib` contains modules for analyzing
AYO and EXOSIMS, but can be easily extended to support other yield codes.

# Methods and Functionality

## Parsing and Getting Values

`yieldplotlib` provides a loading system with a unified interface for accessing data from
the yield codes. The system internally manages the complex and inconsistent file structures of the
AYO and EXOSIMS inputs and outputs so that
users can access data with simple and consistent queries.
For collaboration purposes, the valid queries are managed in a Google
Sheet (see \autoref{fig:key_map_csv}) and automatically processed into a universal key map.

![Example portion of the `yieldplotlib` key map containing the
mappings between AYO, EXOSIMS, and `yieldplotlib` parameters.\label{fig:key_map_csv}](figures/ypl_csv_table.jpeg)

## Plotting

### Generic and Comparison Plots

`yieldplotlib` extends the widely used Python plotting library `matplotlib`, leveraging
its extensive customization options and the familiarity many users will already have with it.
The `yieldplotlib` generic
plots (`ypl_plot`, `ypl_scatter`, and `ypl_hist`) are used for single yield run visualizations.

To compare multiple yield runs, `yieldplotlib` also provides a set of flexible comparison plots
that create multi-panel figures to quickly identify discrepancies.

In order to generate summary plots quickly, `yieldplotlib` provides a command line interface
and plotting pipeline to create a suite of commonly used yield plots.

### Plotting Scripts

`yieldplotlib` contains scripts for generating common plots used in yield code visualizations. These
allow users to instantly compare AYO and EXOSIMS results as motivated by the rapid progress of HWO's
ongoing architecture trade studies. These scripts also function as examples
for users who want to adapt the generic `yieldplotlib` methods to
generate bespoke visualizations.

\autoref{fig:hz_completeness} compares the mission's "habitable zone completeness", the
probability that the simulated mission's observations would detect a planet in the habitable zone if one exists,
as calculated by the two yield codes side-by-side.
\autoref{fig:planet_hists} shows histograms of the total number of detected
planets found as a function of planet type for the two codes though, in this example, the inputs to each code
also differ resulting in the seen discrepancies.

![Plot of the Habitable Zone (HZ) completeness as a function of host star luminosity (in units of
Solar luminosity) and distance (in parsecs). Here the AYO results are on the left and the EXOSIMS
results are on the right.\label{fig:hz_completeness}](figures/hz_completeness.png)

![Bar chart comparing AYO and EXOSIMS planet
yields for different classes of planets. This plot demonstrates
`yieldplotlib`'s usage of the `mplcyberpunk` color scheme as an alternative
dark mode style. Note that this is a demonstration plot only, the AYO and EXOSIMS
inputs shown are not directly comparable.
\label{fig:planet_hists}](figures/comparative_bar_plot_grouped.png)

Yield code inputs have a profound impact on calculated yield and plotting them
is important to ensure consistency.
Yield input packages (YIPs), a set of files that describe
coronagraph performance, can also be loaded and accessed in `yieldplotlib`
to compare how different codes process the same input coronagraph.
\autoref{fig:core_throughput} shows a comparison of the calculated coronagraph throughput
for both the two codes studied, and as accessed via an additional YIP analysis tool called `yippy`.
Smaller throughputs result in less planet light on the detector
which can result in lower yields.

![Core throughput vs. separation (in $\lambda$/D) for the same coronagraph
when processed by AYO, EXOSIMS, and calculated by a tool named `yippy`.
The differences are due to the different interpolation
methods used and the definition of aperture over which the throughput is calculated. This highlights
the types of insights that tools like `yieldplotlib` can help to uncover.
\label{fig:core_throughput}](figures/core_throughput_all_curves.jpeg)

# Future Work

A new cross-calibration study
of yield codes is being organized and will utilize `yieldplotlib`. This study will be vital to
the ongoing HWO architecture trade studies and ensure more reliable and robust yield estimates.

# Acknowledgements

Corey Spohn’s research was supported by an appointment to the NASA Postdoctoral Program at the NASA
Goddard Space Flight Center, administered by Oak Ridge Associated Universities under contract with NASA.
Sarah Steiger acknowledges support from an STScI Postdoctoral Fellowship.

The authors would also like to acknowledge Christopher Stark, Dmitry Savransky, Rhonda Morgan, and
Armen Tokadjian for providing consultation on the AYO and EXOSIMS repositories. They would also like
to thank Justin Hom, and the rest of the Exoplanet Science Yields Working Group (ESYWG) for
their valuable feedback and discussions as well as Susan Redmond for the development of the sample Yield
Input Package.
