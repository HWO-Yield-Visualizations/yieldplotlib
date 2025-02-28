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

Determining the expected amount of detected and characterized exoplanets for proposed flagship space 
observatories such as the upcoming Habitable Worlds Observatory is essential for performing key 
architecture trades and ensuring the success of the mission. There are many of these ``yield'' 
codes that perform these complex calculations which non-exhaustively include simulating 
astrophysical scenes, simulating observatory performance, scheduling observations, and performing 
exposure time calculations. Being able to directly compare and visualize the inputs and output of
these yield codes is important 

# Statement of need

Expected exoplanetary yield is an important metric when evaluating the success of proposed
flagship space observatory architectures such as those currently being considered for the Habitable 
Worlds Observatory (HWO; @HWOFeinberg2024). As HWO is being developed and trade spaces are 
explored, yield codes such as the Altruistic Yield Optimizer (AYO; @AYO2014) and EXOSIMS 
[@EXOSIMS2016] that can calculate the expected number of detected and characterized planets for a 
given mission architecture are essential. While these yield codes have the same goal, they can be 
complex and have major differences in their inputs and outputs that has made comparing results 
difficult. The need for a unified library for visualizing the inputs and outputs of these yield 
codes in a complete, descriptive, and accessible way has therefore also become apparent. This is 
non-trivial due to the differing syntaxes, structures, and assumptions that each of these codes
make. 

When these values are interrogated directly, however, new insights are achieved. This is 
highlighted in detail in @ETCCrossCal2025 where a comparison of just the internal exposure time 
calculations of AYO and EXOSIMS was done and both errors and sources of previously unknown 
discrepancy were found. `yieldplotlib` is in many ways a continuation of that initial work but 
aimed instead at the higher level yield products which are of the most direct interest. 

`yieldplotlib` is a Python package for visualizing the inputs and outputs of AYO and EXOSIMS 
through the use of a loading and parsing structure that allows for the easy access of keywords 
in each code that represent the same quantity. 

`yieldplotlib` is designed to communicate the results of yield codes to the broader community and 
produce publication-quality plots without the need to understand the complex yield codes that were 
used to generate the data. Currently `yieldplotlib` contains modules for analyzing AYO and EXOSIMS, 
but is easily extensible and support for other yield codes can be easily added in the future.

# Methods and Functionality 

## Parsing and Getting Values
`yieldplotlib` uses a file node and directory structure to parse the yield output or input packages 
from AYO and EXOSIMS. It then uses a user generated `key_map` to link the EXOSIMS and AYO keys to a 
universal key in `yieldplotlib`. This `key_map` is automatically generated from a CSV file which 
has a stable version hosted locally on the repository and an active development version on Google 
Sheets for broader collaboration. An example few lines from the CSV file can be Found in Table ??.

Once the yield packages are parsed a getter can be called on the directories 
(i.e. `ayo.get('yield_earth')`) to return the corresponding value from the yield code.  

## Plotting

`yieldplotlib` contains scripts for generating common plots used in yield code visualizations to 
provide instant usability for comparing AYO and EXOSIMS as motivated by rapid pace of the ongoing 
architecture trade studies for HWO. This also serves to provide examples on how the package can be 
used for those who want to use the `yieldplotlib` structure to generate their own visualizations. 

Figure \autoref{fig:hz_completeness} and Figure \autoref{fig:planet_hists} show two different types 
of yield outputs. Figure \autoref{fig:hz_completeness} shows the the fraction of a star's habitable 
zone that cen be sampled by during the lifetime of a mission known as the ``habitable zone 
completeness'' with the two yield codes in side by side axes and using the same color bar for ease
of comparison. Figure \autoref{fig:planet_hists} shows histograms of the total number of detected 
planets foudn for each yield code as a function of planet type.

![Plot of the Habitable Zone (HZ) completeness as a function of host star luminosity (in units of 
Solar luminosity) and distance (in parsecs). Here the AYO results are on the left and the EXOSIMS 
results are on the right.\label{fig:hz_completeness}](figures/TEMP_hz_completeness.jpeg)

![Bar chart showing expected EXOSIMS planet yields for hot (pink), warm (yellow), and cold (blue)
Rocky planets, Super Earths, Sub-Neptunes, Neptunes and Jupiters.
\label{fig:planet_hists}](figures/TEMP_planet_histograms.jpeg)

Yield code inputs can also have a profound impact on their calculations and so plottign these 
values is also important to ensure consistency. Figure \autoref{fig:core_throughput} shows the 
throughput for a key series of optics in the observatory known as a coronagraph. Smaller 
throughputs mean less planet late makes it onto the detector and can have a profound impact on 
yields. 

![Core throughput vs. separation (in lambda/D) for the amplitude apodized vortex coronagraph 
assumed by AYO (dotted yellow), EXOSIMS (dashed pink) and pulled directly from the yield input 
package using yippy (solid blue). Slight differences between the codes can be attributed to how 
the "core" is defined. EXOSIMS and yippy adopt a fixed radius circular aperture whereas AYO 
defines an aperture based on pixels having more than 30% of the peak flux. Additional sources 
of difference can also lie in the interpolation methods used by all of the codes.
\label{fig:core_throughput}](figures/TEMP_core_throughput.jpg)

## Pipeline and Command Line Interface 

# Acknowledgements

S.S. acknowledges support from an STScI Postdoctoral Fellowship.

The authors would also like to acknowledge Christopher Stark, Dmitry Savransky, Rhonda Morgan, and 
Armen Tokadjian for providing consultation on the AYO and EXOSIMS repositories.
