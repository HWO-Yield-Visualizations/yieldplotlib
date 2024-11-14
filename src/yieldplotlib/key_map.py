"""Key mapping for yieldplotlib library."""

KEY_MAP = {
    "star_id": {
        "EXOSIMSCSVFile": {"file": "reduce-star-target.csv", "name": "star_sInd"},
        "AYOCSVFile": {"file": "target_list.csv", "name": "starID"},
        "comment": "",
    },
    "star_name": {
        "EXOSIMSCSVFile": {"file": "reduce-star-target.csv", "name": "star_Name"},
        "AYOCSVFile": {"file": "target_list.csv", "name": "HIP"},
        "comment": "",
    },
    "star_L": {
        "EXOSIMSCSVFile": {"file": "reduce-star-target.csv", "name": "star_L"},
        "AYOCSVFile": {"file": "target_list.csv", "name": "Lstar (sun)"},
        "comment": "",
    },
    "star_dist": {
        "EXOSIMSCSVFile": {"file": "reduce-star-target.csv", "name": "star_dist"},
        "AYOCSVFile": {"file": "target_list.csv", "name": "dist (pc)"},
        "comment": "",
    },
    "star_spec": {
        "EXOSIMSCSVFile": {"file": "reduce-star-target.csv", "name": "star_Spec"},
        "AYOCSVFile": {"file": "target_list.csv", "name": "Type"},
        "comment": "",
    },
    "exp_time_char": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_tInt_mean",
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total Spec Char Time (days)",
        },
        "comment": "",
    },
    "star_comp_det": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_cume_mean",
        },
        "AYOCSVFile": {"file": "target_list.csv", "name": "Total HZ Completeness"},
        "comment": "The EXOSIMS value is not guaranteed to be habitable zone but AYO is",
    },
    "exp_time_det": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_tInt_mean",
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total BB Imaging Time (days)",
        },
        "comment": "",
    },
    "obs_target_name": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "name"},
        "AYOCSVFile": {"file": "observations.csv", "name": "HIP"},
        "comment": "",
    },
    "obs_target_ind": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "sind"},
        "AYOCSVFile": {"file": "observations.csv", "name": "starID"},
        "comment": "",
    },
    "RA": {"AYOCSVFile": {"file": "target_list.csv", "name": "RA"}, "comment": ""},
    "Dec": {"AYOCSVFile": {"file": "target_list.csv", "name": "Dec"}, "comment": ""},
    "Umag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Umag"}, "comment": ""},
    "Bmag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Bmag"}, "comment": ""},
    "Vmag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Vmag"}, "comment": ""},
    "Rmag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Rmag"}, "comment": ""},
    "Imag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Imag"}, "comment": ""},
    "Jmag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Jmag"}, "comment": ""},
    "Hmag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Hmag"}, "comment": ""},
    "Kmag": {"AYOCSVFile": {"file": "target_list.csv", "name": "Kmag"}, "comment": ""},
    "M_V": {"AYOCSVFile": {"file": "target_list.csv", "name": "M_V"}, "comment": ""},
    "Angdiam (mas)": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "Angdiam (mas)"},
        "comment": "",
    },
    "Mass (Msun)": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "Mass (Msun)"},
        "comment": "",
    },
    "WDS_sep": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "WDS_sep"},
        "comment": "",
    },
    "WDS_dmag": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "WDS_dmag"},
        "comment": "",
    },
    "Detection Coronagraph ID": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "Detection Coronagraph ID"},
        "comment": "",
    },
    "Characterization Coronagraph ID": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Characterization Coronagraph ID",
        },
        "comment": "",
    },
    "Detection Wavelength (microns)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Detection Wavelength (microns)",
        },
        "comment": "",
    },
    "Characterization Wavelength (microns)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Characterization Wavelength (microns)",
        },
        "comment": "",
    },
    "EEID (mas)": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "EEID (mas)"},
        "comment": "",
    },
    "nexozodis (zodis)": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "nexozodis (zodis)"},
        "comment": "",
    },
    "Total EEC Yield": {
        "AYOCSVFile": {"file": "target_list.csv", "name": "Total EEC Yield"},
        "comment": "",
    },
    "Visit #": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Visit #"},
        "comment": "",
    },
    "Visit dt (years)": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Visit dt (years)"},
        "comment": "",
    },
    "Exp Time (days)": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Exp Time (days)"},
        "comment": "",
    },
    "Spec char time (days)": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Spec char time (days)"},
        "comment": "",
    },
    "yield_earth": {
        "AYOCSVFile": {"file": "observations.csv", "name": "exoEarth candidate yield"},
        "comment": "",
    },
    "yield_hot_rocky": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Hot Rocky yield"},
        "comment": 'AYO reports these on a per-observation basis, EXOSIMS reports the mission average and many other parameters (h_RpL_det_main_mean is the unique detections, h_RpL_population_mean includes revisit observations, not sure what the "alt_" ones are)',
    },
    "yield_warm_rocky": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Warm Rocky yield"},
        "comment": "",
    },
    "yield_cold_rocky": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Cold Rocky yield"},
        "comment": "",
    },
    "yield_hot_super_earth": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Hot SuperEarth yield"},
        "comment": "",
    },
    "yield_warm_super_earth": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Warm SuperEarth yield"},
        "comment": "",
    },
    "yield_cold_super_earth": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Cold SuperEarth yield"},
        "comment": "",
    },
    "yield_hot_sub_neptune": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Hot Sub-Neptune yield"},
        "comment": "",
    },
    "yield_warm_sub_neptune": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Warm Sub-Neptune yield"},
        "comment": "",
    },
    "yield_cold_sub_neptune": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Cold Sub-Neptune yield"},
        "comment": "",
    },
    "yield_hot_neptune": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Hot Neptune yield"},
        "comment": "",
    },
    "yield_warm_neptune": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Warm Neptune yield"},
        "comment": "",
    },
    "yield_cold_neptune": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Cold Neptune yield"},
        "comment": "",
    },
    "yield_hot_jupiter": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Hot Jupiter yield"},
        "comment": "",
    },
    "yield_warm_jupiter": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Warm Jupiter yield"},
        "comment": "",
    },
    "yield_cold_jupiter": {
        "AYOCSVFile": {"file": "observations.csv", "name": "Cold Jupiter yield"},
        "comment": "",
    },
    "chars_earth_strict": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "chars_earth_strict"},
        "comment": "",
    },
    "chars_earth_unique": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "chars_earth_unique"},
        "comment": "",
    },
    "chars_strict_mean": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "chars_strict_mean"},
        "comment": "",
    },
    "chars_unique_mean": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "chars_unique_mean"},
        "comment": "",
    },
    "detections_earth_all": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "detections_earth_all"},
        "comment": "",
    },
    "detections_earth_unique": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_earth_unique",
        },
        "comment": "",
    },
    "detections_unique_mean": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "detections_unique_mean"},
        "comment": "",
    },
    "ensemble_size": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "ensemble_size"},
        "comment": "",
    },
    "experiment": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "experiment"},
        "comment": "",
    },
    "runtime": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "runtime"},
        "comment": "",
    },
    "simtime": {
        "EXOSIMSCSVFile": {"file": "reduce-info.csv", "name": "simtime"},
        "comment": "",
    },
    "h_star_char_comp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_comp_mean",
        },
        "comment": "",
    },
    "h_star_char_earth_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_cume_mean",
        },
        "comment": "",
    },
    "h_star_char_earth_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_frac_mean",
        },
        "comment": "",
    },
    "h_star_char_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_uniq_mean",
        },
        "comment": "",
    },
    "h_star_char_earth_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_value_mean",
        },
        "comment": "",
    },
    "h_star_char_plan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_cume_mean",
        },
        "comment": "",
    },
    "h_star_char_plan_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_frac_mean",
        },
        "comment": "",
    },
    "h_star_char_plan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_uniq_mean",
        },
        "comment": "",
    },
    "h_star_char_plan_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_value_mean",
        },
        "comment": "",
    },
    "h_star_char_tobs1_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_tobs1_mean",
        },
        "comment": "",
    },
    "h_star_char_visit_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_visit_mean",
        },
        "comment": "",
    },
    "h_star_det_comp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_comp_mean",
        },
        "comment": "",
    },
    "h_star_det_earth_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_frac_mean",
        },
        "comment": "",
    },
    "h_star_det_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_uniq_mean",
        },
        "comment": "",
    },
    "h_star_det_earth_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_value_mean",
        },
        "comment": "",
    },
    "h_star_det_plan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_cume_mean",
        },
        "comment": "",
    },
    "h_star_det_plan_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_frac_mean",
        },
        "comment": "",
    },
    "h_star_det_plan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_uniq_mean",
        },
        "comment": "",
    },
    "h_star_det_plan_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_value_mean",
        },
        "comment": "",
    },
    "h_star_det_tobs1_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_tobs1_mean",
        },
        "comment": "",
    },
    "h_star_det_visit_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_visit_mean",
        },
        "comment": "",
    },
    "h_star_earth_per_star_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_earth_per_star_mean",
        },
        "comment": "",
    },
    "h_star_plan_per_star_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_plan_per_star_mean",
        },
        "comment": "",
    },
    "h_star_promo_allplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_allplan_mean",
        },
        "comment": "",
    },
    "h_star_promo_earth_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_earth_mean",
        },
        "comment": "",
    },
    "h_star_promo_hzone_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_hzone_mean",
        },
        "comment": "",
    },
    "h_visit_bins_mean": {
        "EXOSIMSCSVFile": {"file": "reduce-visits.csv", "name": "h_visit_bins_mean"},
        "comment": "",
    },
    "h_visit_all_mean": {
        "EXOSIMSCSVFile": {"file": "reduce-visits.csv", "name": "h_visit_all_mean"},
        "comment": "",
    },
    "h_visit_earth_mean": {
        "EXOSIMSCSVFile": {"file": "reduce-visits.csv", "name": "h_visit_earth_mean"},
        "comment": "",
    },
    "h_det_time_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_det_time_lo_mean",
        },
        "comment": "",
    },
    "h_det_time_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_det_time_hi_mean",
        },
        "comment": "",
    },
    "h_time_char_full_allplan_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_cume_red_mean",
        },
        "comment": "",
    },
    "h_time_char_full_allplan_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_cume_union_mean",
        },
        "comment": "",
    },
    "h_time_char_full_allplan_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_revi_red_mean",
        },
        "comment": "",
    },
    "h_time_char_full_allplan_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_revi_union_mean",
        },
        "comment": "",
    },
    "h_time_char_full_allplan_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_uniq_red_mean",
        },
        "comment": "",
    },
    "h_time_char_full_allplan_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_uniq_union_mean",
        },
        "comment": "",
    },
    "h_time_char_full_earth_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_cume_red_mean",
        },
        "comment": "",
    },
    "h_time_char_full_earth_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_cume_union_mean",
        },
        "comment": "",
    },
    "h_time_char_full_earth_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_revi_red_mean",
        },
        "comment": "",
    },
    "h_time_char_full_earth_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_revi_union_mean",
        },
        "comment": "",
    },
    "h_time_char_full_earth_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_uniq_red_mean",
        },
        "comment": "",
    },
    "h_time_char_full_earth_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_uniq_union_mean",
        },
        "comment": "",
    },
    "h_time_char_part_allplan_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_cume_red_mean",
        },
        "comment": "",
    },
    "h_time_char_part_allplan_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_cume_union_mean",
        },
        "comment": "",
    },
    "h_time_char_part_allplan_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_revi_red_mean",
        },
        "comment": "",
    },
    "h_time_char_part_allplan_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_revi_union_mean",
        },
        "comment": "",
    },
    "h_time_char_part_allplan_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_uniq_red_mean",
        },
        "comment": "",
    },
    "h_time_char_part_allplan_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_uniq_union_mean",
        },
        "comment": "",
    },
    "h_time_char_part_earth_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_cume_red_mean",
        },
        "comment": "",
    },
    "h_time_char_part_earth_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_cume_union_mean",
        },
        "comment": "",
    },
    "h_time_char_part_earth_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_revi_red_mean",
        },
        "comment": "",
    },
    "h_time_char_part_earth_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_revi_union_mean",
        },
        "comment": "",
    },
    "h_time_char_part_earth_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_uniq_red_mean",
        },
        "comment": "",
    },
    "h_time_char_part_earth_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_uniq_union_mean",
        },
        "comment": "",
    },
    "h_time_det_allplan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_cume_mean",
        },
        "comment": "",
    },
    "h_time_det_allplan_revi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_revi_mean",
        },
        "comment": "",
    },
    "h_time_det_allplan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_uniq_mean",
        },
        "comment": "",
    },
    "h_time_det_earth_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_cume_mean",
        },
        "comment": "",
    },
    "h_time_det_earth_revi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_revi_mean",
        },
        "comment": "",
    },
    "h_time_det_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_uniq_mean",
        },
        "comment": "",
    },
    "h_earth_char_count_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_count_lo_mean",
        },
        "comment": "",
    },
    "h_earth_char_count_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_count_hi_mean",
        },
        "comment": "",
    },
    "h_earth_char_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_all_mean",
        },
        "comment": "",
    },
    "h_earth_xchar_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_xchar_all_mean",
        },
        "comment": "",
    },
    "h_earth_char_strict_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_strict_mean",
        },
        "comment": "",
    },
    "ensemble": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "ensemble"},
        "comment": "",
    },
    "obsnum": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "obsnum"},
        "comment": "",
    },
    "pind": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "pind"},
        "comment": "",
    },
    "n_earth": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "n_earth"},
        "comment": "",
    },
    "n_success": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "n_success"},
        "comment": "",
    },
    "is_success": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "is_success"},
        "comment": "",
    },
    "is_deep": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "is_deep"},
        "comment": "",
    },
    "is_promo": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "is_promo"},
        "comment": "",
    },
    "WA": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "WA"},
        "comment": "",
    },
    "dMag": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "dMag"},
        "comment": "",
    },
    "phi": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "phi"},
        "comment": "",
    },
    "char_SNR": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "char_SNR"},
        "comment": "",
    },
    "MV": {
        "EXOSIMSCSVFile": {"file": "reduce-earth-char-list.csv", "name": "MV"},
        "comment": "",
    },
    "exoE_char_full": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_full"},
        "comment": "",
    },
    "exoE_char_part": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_part"},
        "comment": "",
    },
    "exoE_char_snr": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_snr"},
        "comment": "",
    },
    "exoE_char_strict": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_strict"},
        "comment": "",
    },
    "exoE_char_tput_full": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_tput_full"},
        "comment": "",
    },
    "exoE_char_tput_strict": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_tput_strict"},
        "comment": "",
    },
    "exoE_det_alt": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_det_alt"},
        "comment": "",
    },
    "exoE_det_main": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_det_main"},
        "comment": "",
    },
    "exoE_population": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_population"},
        "comment": "",
    },
    "exoE_xchar_full": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_xchar_full"},
        "comment": "",
    },
    "exoE_xchar_part": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_xchar_part"},
        "comment": "",
    },
    "exoE_xchar_snr": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_xchar_snr"},
        "comment": "",
    },
    "exoE_xchar_tput_full": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_xchar_tput_full"},
        "comment": "",
    },
    "exoE_xdet_alt": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_xdet_alt"},
        "comment": "",
    },
    "exoE_xdet_main": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_xdet_main"},
        "comment": "",
    },
    "exoE_char_full_red": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_full_red"},
        "comment": "",
    },
    "exoE_char_part_red": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_part_red"},
        "comment": "",
    },
    "exoE_char_snr_red": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_snr_red"},
        "comment": "",
    },
    "exoE_char_full_union": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_full_union"},
        "comment": "",
    },
    "exoE_char_part_union": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_part_union"},
        "comment": "",
    },
    "exoE_char_snr_union": {
        "EXOSIMSCSVFile": {"file": "reduce-earth.csv", "name": "exoE_char_snr_union"},
        "comment": "",
    },
    "detfunnel_allstar_cand_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_allplan",
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_earth",
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_hzone",
        },
        "comment": "",
    },
    "detfunnel_allstar_cand_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_star",
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det0_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det1_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det2_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det3_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_det4_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_detV_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_iwa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_owa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_f_snr_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_allplan_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_earth_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_hzone_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_fails_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_star_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_allplan_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_earth_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_hzone_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_success_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_star_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_allplan_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_earth_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_hzone_uniq",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_star_cume",
        },
        "comment": "",
    },
    "detfunnel_allstar_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_star_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_cand_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_allplan",
        },
        "comment": "",
    },
    "detfunnel_promo_cand_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_earth",
        },
        "comment": "",
    },
    "detfunnel_promo_cand_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_hzone",
        },
        "comment": "",
    },
    "detfunnel_promo_cand_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_star",
        },
        "comment": "",
    },
    "detfunnel_promo_det0_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det0_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det0_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det0_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det1_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det1_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det1_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det1_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det2_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det2_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det2_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det2_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det3_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det3_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det3_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det3_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det4_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det4_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det4_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_det4_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_detV_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_detV_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_detV_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_detV_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_iwa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_owa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_f_snr_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_allplan_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_earth_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_hzone_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_fails_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_star_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_success_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_success_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_allplan_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_success_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_success_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_earth_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_success_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_success_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_hzone_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_success_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_success_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_star_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_allplan_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_allplan_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_earth_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_earth_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_hzone_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_hzone_uniq",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_star_cume",
        },
        "comment": "",
    },
    "detfunnel_promo_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_star_uniq",
        },
        "comment": "",
    },
    "h_event_count_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_lo_mean",
        },
        "comment": "",
    },
    "h_event_count_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_hi_mean",
        },
        "comment": "",
    },
    "h_event_count_char_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_char_mean",
        },
        "comment": "",
    },
    "h_event_count_char_rvplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_char_rvplan_mean",
        },
        "comment": "",
    },
    "h_event_count_det_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_det_mean",
        },
        "comment": "",
    },
    "h_event_count_det_rvplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_det_rvplan_mean",
        },
        "comment": "",
    },
    "h_event_count_detp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_detp_mean",
        },
        "comment": "",
    },
    "h_event_count_slew_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_slew_mean",
        },
        "comment": "",
    },
    "h_event_b0_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b0_duration_lo_mean",
        },
        "comment": "",
    },
    "h_event_b0_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b0_duration_hi_mean",
        },
        "comment": "",
    },
    "h_event_b1_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b1_duration_lo_mean",
        },
        "comment": "",
    },
    "h_event_b1_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b1_duration_hi_mean",
        },
        "comment": "",
    },
    "h_event_b2_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b2_duration_lo_mean",
        },
        "comment": "",
    },
    "h_event_b2_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b2_duration_hi_mean",
        },
        "comment": "",
    },
    "h_event_char_b0_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b0_duration_mean",
        },
        "comment": "",
    },
    "h_event_char_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b1_duration_mean",
        },
        "comment": "",
    },
    "h_event_char_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b2_duration_mean",
        },
        "comment": "",
    },
    "h_event_det_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_det_b1_duration_mean",
        },
        "comment": "",
    },
    "h_event_det_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_det_b2_duration_mean",
        },
        "comment": "",
    },
    "h_event_slew_b0_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b0_duration_mean",
        },
        "comment": "",
    },
    "h_event_slew_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b1_duration_mean",
        },
        "comment": "",
    },
    "h_event_slew_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b2_duration_mean",
        },
        "comment": "",
    },
    "funnel_deep_allplan": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_deep_allplan"},
        "comment": "",
    },
    "funnel_deep_chars_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_allplan_cume",
        },
        "comment": "",
    },
    "funnel_deep_chars_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_allplan_uniq",
        },
        "comment": "",
    },
    "funnel_deep_chars_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_earth_cume",
        },
        "comment": "",
    },
    "funnel_deep_chars_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_earth_uniq",
        },
        "comment": "",
    },
    "funnel_deep_chars_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_hzone_cume",
        },
        "comment": "",
    },
    "funnel_deep_chars_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_hzone_uniq",
        },
        "comment": "",
    },
    "funnel_deep_chars_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_star_cume",
        },
        "comment": "",
    },
    "funnel_deep_chars_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_star_uniq",
        },
        "comment": "",
    },
    "funnel_deep_earth": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_deep_earth"},
        "comment": "",
    },
    "funnel_deep_hzone": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_deep_hzone"},
        "comment": "",
    },
    "funnel_deep_star": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_deep_star"},
        "comment": "",
    },
    "funnel_deep_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_allplan_cume",
        },
        "comment": "",
    },
    "funnel_deep_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_allplan_uniq",
        },
        "comment": "",
    },
    "funnel_deep_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_earth_cume",
        },
        "comment": "",
    },
    "funnel_deep_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_earth_uniq",
        },
        "comment": "",
    },
    "funnel_deep_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_hzone_cume",
        },
        "comment": "",
    },
    "funnel_deep_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_hzone_uniq",
        },
        "comment": "",
    },
    "funnel_deep_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_star_cume",
        },
        "comment": "",
    },
    "funnel_deep_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_star_uniq",
        },
        "comment": "",
    },
    "funnel_promo_allplan": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_promo_allplan"},
        "comment": "",
    },
    "funnel_promo_chars_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_allplan_cume",
        },
        "comment": "",
    },
    "funnel_promo_chars_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_allplan_uniq",
        },
        "comment": "",
    },
    "funnel_promo_chars_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_earth_cume",
        },
        "comment": "",
    },
    "funnel_promo_chars_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_earth_uniq",
        },
        "comment": "",
    },
    "funnel_promo_chars_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_hzone_cume",
        },
        "comment": "",
    },
    "funnel_promo_chars_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_hzone_uniq",
        },
        "comment": "",
    },
    "funnel_promo_chars_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_star_cume",
        },
        "comment": "",
    },
    "funnel_promo_chars_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_star_uniq",
        },
        "comment": "",
    },
    "funnel_promo_earth": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_promo_earth"},
        "comment": "",
    },
    "funnel_promo_hzone": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_promo_hzone"},
        "comment": "",
    },
    "funnel_promo_star": {
        "EXOSIMSCSVFile": {"file": "reduce-funnel.csv", "name": "funnel_promo_star"},
        "comment": "",
    },
    "funnel_promo_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_allplan_cume",
        },
        "comment": "",
    },
    "funnel_promo_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_allplan_uniq",
        },
        "comment": "",
    },
    "funnel_promo_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_earth_cume",
        },
        "comment": "",
    },
    "funnel_promo_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_earth_uniq",
        },
        "comment": "",
    },
    "funnel_promo_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_hzone_cume",
        },
        "comment": "",
    },
    "funnel_promo_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_hzone_uniq",
        },
        "comment": "",
    },
    "funnel_promo_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_star_cume",
        },
        "comment": "",
    },
    "funnel_promo_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_star_uniq",
        },
        "comment": "",
    },
}
