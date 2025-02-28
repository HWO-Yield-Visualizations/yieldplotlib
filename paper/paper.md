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


# Acknowledgements

S.S. acknowledges support from an STScI Postdoctoral Fellowship.

The authors would also like to acknowledge Christopher Stark, Dmitry Savransky, Rhonda Morgan, and 
Armen Tokadjian for providing consultation on the AYO and EXOSIMS repositories.
