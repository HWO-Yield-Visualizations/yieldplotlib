"""Key mapping for yieldplotlib library."""

KEY_MAP = {
    "star_id": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_sInd",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "starID",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "star_name": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_Name",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "HIP",
            "transform": {"type": "custom", "value": None},
        },
        "comment": "",
    },
    "star_L": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_L",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Lstar (sun)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "star_dist": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_dist",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "dist (pc)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "star_spec": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_Spec",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Type",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exp_time_char": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_tInt_mean",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total Spec Char Time (days)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "star_comp_det": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_cume_mean",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total HZ Completeness",
            "transform": {"type": "none", "value": None},
        },
        "comment": "The EXOSIMS value is not guaranteed to be habitable zone but AYO is",
    },
    "exp_time_det": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_tInt_mean",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total BB Imaging Time (days)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "obs_target_name": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "name",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "HIP",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "obs_target_ind": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "sind",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "starID",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "yield_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_det_alt_mean",
            "transform": {"type": "none", "value": None},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "exoEarth candidate yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_hot_rocky": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 0},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Rocky yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": 'AYO reports these on a per-observation basis, EXOSIMS reports the mission average and many other parameters (h_RpL_det_main_mean is the unique detections, h_RpL_population_mean includes revisit observations, not sure what the "alt_" ones are)',
    },
    "yield_warm_rocky": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 1},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Rocky yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_cold_rocky": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 2},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Rocky yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_hot_super_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 3},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot SuperEarth yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_warm_super_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 4},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm SuperEarth yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_cold_super_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 5},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold SuperEarth yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_hot_sub_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 6},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Sub-Neptune yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_warm_sub_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 7},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Sub-Neptune yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_cold_sub_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 8},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Sub-Neptune yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_hot_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 9},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Neptune yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_warm_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 10},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Neptune yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_cold_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 11},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Neptune yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_hot_jupiter": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 12},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Jupiter yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_warm_jupiter": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 13},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Jupiter yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "yield_cold_jupiter": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "transform": {"type": "index", "value": 14},
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Jupiter yield",
            "transform": {"type": "sum", "value": None},
        },
        "comment": "",
    },
    "RA": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "RA",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Dec": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Dec",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Umag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Umag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Bmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Bmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Vmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Vmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Rmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Rmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Imag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Imag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Jmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Jmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Hmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Hmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Kmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Kmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "M_V": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "M_V",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Angdiam (mas)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Angdiam (mas)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Mass (Msun)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Mass (Msun)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "WDS_sep": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "WDS_sep",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "WDS_dmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "WDS_dmag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Detection Coronagraph ID": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Detection Coronagraph ID",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Characterization Coronagraph ID": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Characterization Coronagraph ID",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Detection Wavelength (microns)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Detection Wavelength (microns)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Characterization Wavelength (microns)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Characterization Wavelength (microns)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "EEID (mas)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "EEID (mas)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "nexozodis (zodis)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "nexozodis (zodis)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Total EEC Yield": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total EEC Yield",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Visit #": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Visit #",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Visit dt (years)": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Visit dt (years)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Exp Time (days)": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Exp Time (days)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "Spec char time (days)": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Spec char time (days)",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "chars_earth_strict": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_earth_strict",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "chars_earth_unique": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_earth_unique",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "chars_strict_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_strict_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "chars_unique_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_unique_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detections_earth_all": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_earth_all",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detections_earth_unique": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_earth_unique",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detections_unique_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_unique_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "ensemble_size": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "ensemble_size",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "experiment": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "experiment",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "runtime": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "runtime",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "simtime": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "simtime",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_comp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_comp_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_earth_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_cume_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_earth_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_frac_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_uniq_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_earth_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_value_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_plan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_cume_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_plan_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_frac_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_plan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_uniq_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_plan_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_value_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_tobs1_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_tobs1_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_char_visit_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_visit_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_comp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_comp_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_earth_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_frac_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_uniq_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_earth_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_value_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_plan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_cume_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_plan_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_frac_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_plan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_uniq_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_plan_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_value_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_tobs1_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_tobs1_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_det_visit_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_visit_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_earth_per_star_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_earth_per_star_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_plan_per_star_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_plan_per_star_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_promo_allplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_allplan_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_promo_earth_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_earth_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_star_promo_hzone_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_hzone_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_visit_bins_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-visits.csv",
            "name": "h_visit_bins_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_visit_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-visits.csv",
            "name": "h_visit_all_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_visit_earth_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-visits.csv",
            "name": "h_visit_earth_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_det_time_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_det_time_lo_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_det_time_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_det_time_hi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_allplan_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_cume_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_allplan_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_cume_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_allplan_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_revi_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_allplan_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_revi_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_allplan_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_uniq_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_allplan_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_uniq_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_earth_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_cume_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_earth_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_cume_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_earth_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_revi_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_earth_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_revi_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_earth_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_uniq_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_full_earth_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_uniq_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_allplan_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_cume_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_allplan_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_cume_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_allplan_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_revi_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_allplan_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_revi_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_allplan_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_uniq_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_allplan_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_uniq_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_earth_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_cume_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_earth_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_cume_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_earth_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_revi_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_earth_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_revi_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_earth_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_uniq_red_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_char_part_earth_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_uniq_union_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_det_allplan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_cume_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_det_allplan_revi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_revi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_det_allplan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_uniq_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_det_earth_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_cume_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_det_earth_revi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_revi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_time_det_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_uniq_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_earth_char_count_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_count_lo_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_earth_char_count_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_count_hi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_earth_char_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_all_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_earth_xchar_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_xchar_all_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_earth_char_strict_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_strict_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "ensemble": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "ensemble",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "obsnum": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "obsnum",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "pind": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "pind",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "n_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "n_earth",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "n_success": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "n_success",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "is_success": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "is_success",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "is_deep": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "is_deep",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "is_promo": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "is_promo",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "WA": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "WA",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "dMag": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "dMag",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "phi": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "phi",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "char_SNR": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "char_SNR",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "MV": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "MV",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_full",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_part": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_part",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_snr": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_snr",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_strict": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_strict",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_tput_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_tput_full",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_tput_strict": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_tput_strict",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_det_alt": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_det_alt",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_det_main": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_det_main",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_population": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_population",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_xchar_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_full",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_xchar_part": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_part",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_xchar_snr": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_snr",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_xchar_tput_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_tput_full",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_xdet_alt": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xdet_alt",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_xdet_main": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xdet_main",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_full_red": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_full_red",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_part_red": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_part_red",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_snr_red": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_snr_red",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_full_union": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_full_union",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_part_union": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_part_union",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "exoE_char_snr_union": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_snr_union",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_allplan",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_earth",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_hzone",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_star",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_success_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_cand_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_allplan",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_cand_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_earth",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_cand_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_hzone",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_cand_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_star",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det0_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det0_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det0_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det0_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det1_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det1_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det1_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det1_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det2_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det2_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det2_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det2_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det3_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det3_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det3_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det3_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det4_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det4_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det4_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_det4_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_detV_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_detV_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_detV_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_detV_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_fails_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_success_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "detfunnel_promo_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_lo_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_hi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_char_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_char_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_char_rvplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_char_rvplan_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_det_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_det_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_det_rvplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_det_rvplan_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_detp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_detp_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_count_slew_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_slew_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_b0_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b0_duration_lo_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_b0_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b0_duration_hi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_b1_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b1_duration_lo_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_b1_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b1_duration_hi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_b2_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b2_duration_lo_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_b2_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b2_duration_hi_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_char_b0_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b0_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_char_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b1_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_char_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b2_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_det_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_det_b1_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_det_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_det_b2_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_slew_b0_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b0_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_slew_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b1_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "h_event_slew_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b2_duration_mean",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_allplan",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_chars_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_earth",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_hzone",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_star",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_deep_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_allplan",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_chars_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_earth",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_hzone",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_star",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_allplan_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_allplan_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_earth_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_earth_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_hzone_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_hzone_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_star_cume",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
    "funnel_promo_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_star_uniq",
            "transform": {"type": "none", "value": None},
        },
        "comment": "",
    },
}
