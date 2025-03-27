---
title: 'yieldplotlib: A unified library for exoplanet yield code visualizations'
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

affiliations:
 - name: Goddard Space Flight Center, United States
   index: 1
 - name: Space Telescope Science Institute, United States
   index: 2

date: 28 February 2025
bibliography: paper.bib
---

# Summary

NASA’s next flagship observatory, as recommended by the Astro2020 decadal survey,
is the Habitable World’s Observatory (HWO) which has the ambitious goal to "search
for biosignatures from a robust number of about ∼25 habitable zone planets and be
a transformative facility for general astrophysics". In the phrasing of this science
goal, the importance of expected exo-Earth yield (the total number of detected habitable
zone planets) on the success of the mission is made apparent. As HWO is being developed
and trade spaces are explored, yield codes such as the Altruistic Yield Optimization (AYO)
and EXOSIMS that can calculate the expected number of detected and characterized planets
for a given mission architecture are essential. While these yield codes have the same goal,
they can be complex and have major differences in their inputs and outputs that has made
comparing results difficult. The need for a unified library for visualizing the inputs
and outputs of these yield codes in a complete, descriptive, and accessible way has therefore
also become apparent. To this end we have developed yieldplotlib, an open-source python
library to communicate the results of yield codes to the broader community and produce
publication-quality plots. Currently, there are modules for analyzing AYO and EXOSIMS,
but yieldplotlib is easily extensible and support for other yield codes can be easily
added in the future.

# Statement of need

Expected exoplanetary yield is an important metric when evaluating the success of proposed
flagship space observatory architectures such as those currently being considered for the Habitable
Worlds Observatory (HWO; @HWOFeinberg2024). As HWO is being developed and trade spaces are
explored, yield codes such as the Altruistic Yield Optimizer (AYO; @AYO2014) and EXOSIMS
[@EXOSIMS2016] that can calculate the expected number of detected and characterized planets for a
given mission architecture are essential. While these yield codes have the same goal, they can be
complex and have major differences in their inputs and outputs that has made comparing results
difficult. The need for a unified library for visualizing these yield codes in a complete, descriptive,
and accessible way has therefore also become apparent. This is non-trivial due to the differing
syntaxes, structures, and assumptions that each of these codes make.

Despite the challenges, when these values are interrogated directly, new insights are achieved.
Some of these insights are highlighted in detail in @ETCCrossCal2025 where a comparison of just
the internal exposure time calculations of AYO and EXOSIMS revealed sources of previously unknown
discrepancy. `yieldplotlib` is a continuation of that initial work, but aimed instead at the higher
level yield products which are of the most direct interest.

`yieldplotlib` is a Python package for visualizing the inputs and outputs of AYO and EXOSIMS
through the use of a custom loading and parsing structure that allows for the easy access of equivalent data
across yield code outputs. `yieldplotlib` is designed to communicate the results of yield codes to the
broader community and produce publication-quality plots without the need to understand the complex
underlying yield codes that were used to generate the data. Currently `yieldplotlib` contains modules
for analyzing AYO and EXOSIMS, but is easily extensible and support for other yield codes can be easily
added in the future.

# Methods and Functionality

## Parsing and Getting Values
`yieldplotlib` uses a file node and directory structure to parse the yield output packages
from AYO and EXOSIMS. It then uses a user generated `key_map` to link the EXOSIMS and AYO keys to a
universal key in `yieldplotlib`. This `key_map` is generated from a CSV file in the repository
which is automatically updated on a daily basis daily from an active development
version hosted on Google Sheets for broader collaboration. An example few lines from the CSV
file can be found in the following table.

![Example portion of the yieldplotlib key map CSV file containing the
mappings between AYO, EXOSIMS, and yieldplotlib parameters.](figures/ypl_csv_table.jpeg)

Once the yield packages are loaded and parsed, a getter can be called on the directories
to return the corresponding value from the respective yield code.

```angular2html
from yieldplotlib.load.ayo_directory import AYODirectory
from yieldplotlib.load.exosims_directory import EXOSIMSDirectory

ayo = AYODirectory(Path("path/to/my/ayo_data"))
exosims = EXOSIMSDirectory(Path("path/to/my/exosims_data"))

ayo.get("yield_earth")
exosims.get("yield_earth")
```

Yield input packages (YIPs) specifying input coronagraph parameters can also be read in and accessed
using the same file node and directory structure. This allows users to access key coronagraph performance
metrics that serve as critical inputs to these yield codes. In order to process the YIPs, `yieldplotlib`
uses `yippy` as a backend, though the user interface is identical to generating the AYO and EXOSIMS directories.

```angular2html
from yieldplotlib.load.yip_directory import YIPDirectory

yip = YIPDirectory(Path("path/to/my/yip_data"))
```

## Plotting

### Generic and Comparison Plots

`yieldplotlib` extends the commonly used Python plotting package `matplotlib` to take advantage
of the wide variety of customization options that  `matplotlib` offers, as well as the extensive
knowledge base many users of `yieldplotlib` will have with that package. The `yieldplotlib` generic
plots are designed to be used for single yield run visualizations and can make scatter plots, standard plots,
and histograms.

The comparison plots are designed for plotting multiple yield runs in either the same multi-panel
figure, or on the same set of axes for more complex comparisons.

### Plotting Scripts
`yieldplotlib` contains scripts for generating common plots used in yield code visualizations to
provide instant usability for comparing AYO and EXOSIMS as motivated by the rapid pace of the ongoing
architecture trade studies for HWO. This also serves to provide examples on how the package can be
used for those who want to adapt the generic `yieldplotlib` parsing structure and plotting methods to
generate their own bespoke visualizations.

\autoref{fig:hz_completeness} and \autoref{fig:planet_hists} show two different types
of yield outputs. \autoref{fig:hz_completeness} shows the fraction of a star's habitable
zone that cen be sampled by during the lifetime of a mission known as the "habitable zone
completeness" with the two yield codes in side by side axes and using the same color bar for ease
of comparison. \autoref{fig:planet_hists} shows histograms of the total number of detected
planets found for each yield code as a function of planet type.

![Plot of the Habitable Zone (HZ) completeness as a function of host star luminosity (in units of
Solar luminosity) and distance (in parsecs). Here the AYO results are on the left and the EXOSIMS
results are on the right.\label{fig:hz_completeness}](figures/hz_completeness.png)

![Bar chart showing expected EXOSIMS planet yields for hot (pink), warm (yellow), and cold (blue)
Rocky planets, Super Earths, Sub-Neptunes, Neptunes and Jupiters. Earth-like planets which are
of the most interest for HWO are shown in green. This plot uses the "cyberpunk"
theme from matplotlib which is supported as a keyword argument to yieldplotlib as a dark mode
alternative to the standard plotting color schemes.
\label{fig:planet_hists}](figures/yield_hist_cyber.png)

Yield code inputs can also have a profound impact on their results and so plotting these
values is important to ensure consistency. \autoref{fig:core_throughput} shows the
throughput for a key series of optics in the observatory known as a coronagraph. Smaller
throughputs mean less planet light makes it onto the detector and can have a profound impact on
final yields.

![Core throughput vs. separation (in lambda/D) for the coronagraph
assumed by AYO (dotted purple), EXOSIMS (dashed pink) and pulled directly from the yield input
package using yippy (solid blue). Slight differences between the codes can be attributed to how
the "core" is defined. EXOSIMS and yippy adopt a fixed radius circular aperture whereas AYO
defines an aperture based on pixels having more than 30% of the peak flux. Additional sources
of difference can also lie in the interpolation methods used by all of the codes. This highlights
the types of insights that tools like yieldplotlib can help to uncover.
\label{fig:core_throughput}](figures/core_throughput_all_curves.jpeg)

## Pipeline and Command Line Interface

In order to generate summary plots quickly, `yieldplotlib` comes packaged with a command line interface
and plotting pipeline to create a suite of commonly used yield plots. This is accessed by running
`run_ypl` and providing a path to a single folder containing the outputs for a single AYO or EXOSIMS run,
or to a directory containing subdirectories of many AYO and EXOSIMS runs.

# Future Work

Following on the completion of the ETC cross-calibration work in @ETCCrossCal2025, a new cross-calibration
of high-level yield products is planned which will utilize `yieldplotlib`. This work will be vital to
the ongoing HWO architecture trade studies by providing more reliable and robust yield estimates, improving
current yield codes, and providing a standard to calibrate potentially new yield codes in the future.

# Acknowledgements

Corey Spohn’s research was supported by an appointment to the NASA Postdoctoral Program at the NASA
Goddard Space Flight Center, administered by Oak Ridge Associated Universities under contract with NASA.
Sarah Steiger acknowledges support from an STScI Postdoctoral Fellowship.

The authors would also like to acknowledge Christopher Stark, Dmitry Savransky, Rhonda Morgan, and
Armen Tokadjian for providing consultation on the AYO and EXOSIMS repositories. They would also like
to thank Alex Howe, Justin Hom, and the rest of the Exoplanet Science Yields Working Group (ESYWG) for
their valuable feedback and discussions.
