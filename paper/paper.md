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

NASA’s next flagship observatory, as recommended by the Astro2020 decadal survey,
is the Habitable World’s Observatory (HWO) which has the ambitious goal to "search
for biosignatures from a robust number of about ~25 habitable zone planets and be
a transformative facility for general astrophysics". The total number of habitable zone planets
detected is referred to as the exo-Earth "yield" and estimating it will be critically important
to HWO's success. As HWO is being developed
and trade spaces are explored, yield codes such as the Altruistic Yield Optimizer (AYO)
and EXOSIMS that can calculate the expected number of detected and characterized planets
for a given mission architecture are essential. While these yield codes have the same goal,
they can be complex and have major differences in their inputs and outputs which makes
comparing results difficult. The need for a unified library for visualizing the inputs
and outputs of these yield codes in a complete, descriptive, and accessible way has therefore
also become apparent. To this end we have developed `yieldplotlib`, an open-source Python
library to communicate the results of yield codes to the broader community and produce
publication-quality plots.

# Statement of need

Expected exoplanet yield is an important metric when evaluating the success of proposed
flagship space observatory architectures such as those currently being considered for the Habitable
Worlds Observatory (HWO; @HWOFeinberg2024). As HWO is being developed and trade spaces are
explored, yield codes such as the Altruistic Yield Optimizer (AYO; @AYO2014) and EXOSIMS
[@EXOSIMS2016] that can calculate the expected number of detected and characterized planets for a
given mission architecture are essential. While these yield codes have the same goal, they are
complex, written in different programming languages (IDL and
Python), calculate yield with different methods, and have
major differences in their inputs and outputs.
The need for a unified library for visualizing these yield codes in a complete, descriptive,
and accessible way has become apparent from cross model validation efforts. This is non-trivial due to the differing
methods, syntaxes, structures, and assumptions that each of these codes make.

Despite the challenges, interrogating the values has already provided valuable insights.
The study @ETCCrossCal2025 compared just
the internal exposure time calculations of AYO and EXOSIMS and revealed previously unknown
discrepancies. `yieldplotlib` is a more ambitious continuation of that work, capable of accessing more
important yield products such as the exo-Earth yield.

To visualize the inputs and outputs of AYO and EXOSIMS, `yieldplotlib` uses a custom loading and
parsing structure to easily access equivalent data across both codes.
This allows `yieldplotlib` to communicate the results of yield codes to the broader community
and produce publication-quality plots without manually processing the complex underlying data.
Currently `yieldplotlib` contains modules for analyzing
AYO and EXOSIMS, but can be easily extended to support other yield codes.

# Methods and Functionality

## Parsing and Getting Values

`yieldplotlib` provides a loading system with a unified interface for accessing data from
the yield codes. The system manages the complex and inconsistent file structures of the
AYO and EXOSIMS inputs and outputs internally so that
users can access data with simple and consistent queries.
For collaboration purposes, the valid queries are managed in a Google
Sheet where collaborators have linked the EXOSIMS and AYO keys to a universal key in `yieldplotlib`.
This Google Sheet is processed into a `key_map` which is updated daily.
An example excerpt from the CSV file can be found in
\autoref{fig:key_map_csv}.

![Example portion of the `yieldplotlib` key map CSV file containing the
mappings between AYO, EXOSIMS, and `yieldplotlib` parameters.\label{fig:key_map_csv}](figures/ypl_csv_table.jpeg)

Yield input packages (YIPs) specifying input coronagraph parameters can also be loaded and accessed
using the same file node and directory structure. This allows users to access key coronagraph performance
metrics that serve as critical inputs to these yield codes.

## Plotting

### Generic and Comparison Plots

`yieldplotlib` extends the widely used Python plotting library `matplotlib`, leveraging
its extensive customization options and the familiarity many users already have with it.
The `yieldplotlib` generic
plots (`ypl_plot`, `ypl_scatter`, and `ypl_hist`) are used for single yield run visualizations.
To compare multiple yield runs, `yieldplotlib` provides a set of flexible comparison plots
that plot the runs against each other in multi-panel figures to quickly identify discrepancies.

### Plotting Scripts

`yieldplotlib` contains scripts for generating common plots used in yield code visualizations. These
allow users to instantly compare AYO and EXOSIMS results for HWO's rapidly progressing
architecture trade studies. These scripts also function as examples
for users who want to adapt the generic `yieldplotlib` methods to
generate bespoke visualizations.

\autoref{fig:hz_completeness} and \autoref{fig:planet_hists} show two different examples of these
types of yield outputs. \autoref{fig:hz_completeness} compares the mission's "habitable zone completeness", the
probability that the simulated mission's observations would detect a planet in the habitable zone if one exists,
as calculated by the two yield codes side-by-side.
\autoref{fig:planet_hists} shows histograms of the total number of detected
planets found as a function of planet type in this case just using EXOSIMS.

![Plot of the Habitable Zone (HZ) completeness as a function of host star luminosity (in units of
Solar luminosity) and distance (in parsecs). Here the AYO results are on the left and the EXOSIMS
results are on the right.\label{fig:hz_completeness}](figures/hz_completeness.png)

![Bar chart showing expected EXOSIMS planet yields for hot (pink), warm (yellow), and cold (blue)
Rocky planets, Super Earths, Sub-Neptunes, Neptunes and Jupiters. Earth-like planets which are
of the most interest for HWO are shown in green. This plot uses the "cyberpunk"
theme from the library `mplcyberpunk` which is supported as a keyword argument to `yieldplotlib` as a dark mode
alternative to the standard plotting color schemes.
\label{fig:planet_hists}](figures/yield_hist_cyber.png)

Yield code inputs have a profound impact on calculated yield and plotting them
is important to ensure consistency. \autoref{fig:core_throughput} shows the
throughput for a key series of starlight suppression optics in the observatory known
collectively as a coronagraph. Smaller throughputs result in less planet light on the detector
which can result in lower yields.

![Core throughput vs. separation (in $\lambda$/D) for the coronagraph
assumed by AYO (dotted purple), EXOSIMS (dashed pink), and pulled directly from the yield input
package using yippy (solid blue). Slight differences between the codes can be attributed to how
the "core" is defined. EXOSIMS and yippy adopt a fixed radius circular aperture whereas AYO
defines an aperture based on pixels having more than 30% of the peak flux. Additional sources
of difference can also lie in the interpolation methods used by all of the codes. This highlights
the types of insights that tools like `yieldplotlib` can help to uncover.
\label{fig:core_throughput}](figures/core_throughput_all_curves.jpeg)

## Pipeline and Command Line Interface

In order to generate summary plots quickly, `yieldplotlib` provides a command line interface
and plotting pipeline to create a suite of commonly used yield plots.

# Future Work

Following up on the ETC cross-calibration work in @ETCCrossCal2025, a new cross-calibration study
of high-level yield products is planned which will utilize `yieldplotlib`. This work will be vital to
the ongoing HWO architecture trade studies by ensuring more reliable and robust yield estimates, improving
current yield codes, and providing a standard on which to calibrate new yield codes in the future.

# Acknowledgements

Corey Spohn’s research was supported by an appointment to the NASA Postdoctoral Program at the NASA
Goddard Space Flight Center, administered by Oak Ridge Associated Universities under contract with NASA.
Sarah Steiger acknowledges support from an STScI Postdoctoral Fellowship.

The authors would also like to acknowledge Christopher Stark, Dmitry Savransky, Rhonda Morgan, and
Armen Tokadjian for providing consultation on the AYO and EXOSIMS repositories. They would also like
to thank Justin Hom, and the rest of the Exoplanet Science Yields Working Group (ESYWG) for
their valuable feedback and discussions as well as Susan Redmond for the development of the sample Yield
Input Package.
