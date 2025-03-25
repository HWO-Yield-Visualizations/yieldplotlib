"""Key mapping for yieldplotlib library."""

KEY_MAP = {
    "angdiam": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Angdiam (mas)",
            "unit": "mas",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "diameter",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "blind_comp_det": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "blind_comp_det",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "blind_comp_det",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "All of this has to be handled custom"
    },
    "blind_comp_spec": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "blind_comp_spec",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "blind_comp_spec",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "All of this has to be handled custom"
    },
    "Bmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Bmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Bmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "cic": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "CIC",
            "unit": "count pix^-1 s^-1",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "det_CIC",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "dark_current": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "idark",
            "unit": "count pix^-1 s^-1",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "det_DC",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Dec": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Dec",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "coords_Dec",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "exp_time_char": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_tInt_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total Spec Char Time (days)",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exp_time_det": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_tInt_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total BB Imaging Time (days)",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Hmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Hmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Hmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "Imag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Imag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Imag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "iwa": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "IWA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "IWA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "For AYO this is a hard cutoff, not the actual IWA of the coronagraph which comes from the YIP. This is also true for EXOSIMS, when the param is set in the observingMode, or manually set in the starlightSuppressionSystem definition (which the obsmode then inherits).  Otherwise, it is the largest IWA-value from the input files in the YIP."
    },
    "Jmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Jmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Jmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "Kmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Kmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Kmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "Ms": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Mass (Msun)",
            "unit": "M_sun",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "MsTrue",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "MV": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "MV",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "M_V",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "obs_lam": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "lam",
            "unit": "nm",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "lambda",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "obs_target_ind": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "sind",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "starID",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "obs_target_name": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "name",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "HIP",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "optics_throughput": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "optics",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "Toptical",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "owa": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "OWA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "OWA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "For AYO this is a hard cutoff, not the actual OWA of the coronagraph which comes from the YIP. This is also true for EXOSIMS, when the param is set in the observingMode, or manually set in the starlightSuppressionSystem definition (which the obsmode then inherits).  Otherwise, it is the largest OWA-value from the input files in the YIP."
    },
    "pixel_scale": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "pixelScale",
            "unit": "mas",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "det_pixscale_mas",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "pupil_diam": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "pupilDiam",
            "unit": "meter",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "D",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "qe": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "QE",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "det_QE",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "R": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Rs",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "SR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "RA": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "RA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "coords_RA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "read_noise": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sread",
            "unit": "count pix^-1 read^-1",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "det_RN",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Rmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Rmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Rmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "sc_cic": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_CIC",
            "unit": "count pix^-1 s^-1",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_det_CIC",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_dark_current": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_idark",
            "unit": "count pix^-1 s^-1",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_det_DC",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_obs_lam": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_lam",
            "unit": "nm",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_lambda",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_optics_throughput": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_optics",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_Toptical",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_pixel_scale": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_pixelScale",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_det_pixscale_mas",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_qe": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_QE",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_det_QE",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_R": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_Rs",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_SR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_read_noise": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_sread",
            "unit": "count pix^-1 read^-1",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_det_RN",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_snr": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_SNR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_SNR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "sc_texp": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "sc_texp",
            "unit": "s",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "sc_det_tread",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "snr": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "SNR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "SNR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "star_comp_det": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_cume_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total HZ Completeness",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "The EXOSIMS value is not guaranteed to be habitable zone but AYO is"
    },
    "star_dist": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_dist",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "dist (pc)",
            "unit": "pc",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "star_id": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_sInd",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "starID",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "star_L": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_L",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Lstar (Lsun)",
            "unit": "L_sun",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "star_name": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_Name",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "HIP",
            "unit": "",
            "transform": {
                "type": "custom",
                "value": None
            }
        },
        "comment": ""
    },
    "star_spec": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "star_Spec",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Type",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "texp": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "texp",
            "unit": "s",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOInputFile": {
            "file": "ayo",
            "name": "det_tread",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Umag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Umag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Umag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "Vmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Vmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Vmag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
    "yield_cold_jupiter": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 14
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Jupiter yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_cold_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 11
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Neptune yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_cold_rocky": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 2
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Rocky yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_cold_sub_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 8
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold Sub-Neptune yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_cold_super_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 5
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Cold SuperEarth yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "exoEarth candidate yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_hot_jupiter": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 12
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Jupiter yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_hot_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 9
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Neptune yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_hot_rocky": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 0
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Rocky yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": "AYO reports these on a per-observation basis, EXOSIMS reports the mission average and many other parameters (h_RpL_det_main_mean is the unique detections, h_RpL_population_mean includes revisit observations, not sure what the \"alt_\" ones are)"
    },
    "yield_hot_sub_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 6
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot Sub-Neptune yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_hot_super_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 3
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Hot SuperEarth yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_warm_jupiter": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 13
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Jupiter yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_warm_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 10
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Neptune yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_warm_rocky": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 1
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Rocky yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_warm_sub_neptune": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 7
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm Sub-Neptune yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "yield_warm_super_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-radlum.csv",
            "name": "h_RpL_det_alt_mean",
            "unit": "",
            "transform": {
                "type": "index",
                "value": 4
            }
        },
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Warm SuperEarth yield",
            "unit": "",
            "transform": {
                "type": "sum",
                "value": None
            }
        },
        "comment": ""
    },
    "WDS_sep": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "WDS_sep",
            "unit": "",
            "transform": {
                "type": "custom",
                "value": None
            }
        },
        "comment": ""
    },
    "WDS_dmag": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "WDS_dmag",
            "unit": "",
            "transform": {
                "type": "custom",
                "value": None
            }
        },
        "comment": ""
    },
    "Detection Coronagraph ID": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Detection Coronagraph ID",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Characterization Coronagraph ID": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Characterization Coronagraph ID",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Detection Wavelength (microns)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Detection Wavelength (microns)",
            "unit": "um",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Characterization Wavelength (microns)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Characterization Wavelength (microns)",
            "unit": "um",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "EEID (mas)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "EEID (mas)",
            "unit": "mas",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "nexozodis (zodis)": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "nexozodis (zodis)",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Total EEC Yield": {
        "AYOCSVFile": {
            "file": "target_list.csv",
            "name": "Total EEC Yield",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Visit #": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Visit #",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Visit dt (years)": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Visit dt (years)",
            "unit": "years",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Exp Time (days)": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Exp Time (days)",
            "unit": "days",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Spec char time (days)": {
        "AYOCSVFile": {
            "file": "observations.csv",
            "name": "Spec char time (days)",
            "unit": "days",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "core_thruput": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "core_thruput",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "coron_bw": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "syst_BW",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "coron_lam": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "syst_lam",
            "unit": "nm",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "coron_optics_thorughput": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "syst_optics",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "instruments": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "scienceInstruments",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "istar": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "core_mean_intensity",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "modes": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "observingModes",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "systs": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "starlightSuppressionSystems",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "chars_earth_strict": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_earth_strict",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "chars_earth_unique": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_earth_unique",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "chars_strict_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_strict_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "chars_unique_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "chars_unique_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detections_earth_all": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_earth_all",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detections_earth_unique": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_earth_unique",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detections_unique_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "detections_unique_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "ensemble_size": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "ensemble_size",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "experiment": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "experiment",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "runtime": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "runtime",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "simtime": {
        "EXOSIMSCSVFile": {
            "file": "reduce-info.csv",
            "name": "simtime",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_comp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_comp_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_earth_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_cume_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_earth_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_frac_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_uniq_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_earth_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_earth_value_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_plan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_cume_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_plan_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_frac_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_plan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_uniq_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_plan_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_plan_value_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_tobs1_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_tobs1_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_char_visit_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_char_visit_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_comp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_comp_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS's value here represents the *last* observation of the star made in each DRM, not the first one which is typically what we think of using blind completeness for"
    },
    "h_star_det_earth_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_frac_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_uniq_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_earth_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_earth_value_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_plan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_cume_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_plan_frac_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_frac_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_plan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_uniq_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_plan_value_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_plan_value_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_tobs1_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_tobs1_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_det_visit_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_det_visit_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_earth_per_star_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_earth_per_star_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_plan_per_star_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_plan_per_star_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_promo_allplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_allplan_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_promo_earth_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_earth_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_star_promo_hzone_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-star-target.csv",
            "name": "h_star_promo_hzone_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_visit_bins_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-visits.csv",
            "name": "h_visit_bins_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_visit_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-visits.csv",
            "name": "h_visit_all_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_visit_earth_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-visits.csv",
            "name": "h_visit_earth_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_det_time_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_det_time_lo_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_det_time_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_det_time_hi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_allplan_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_cume_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_allplan_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_cume_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_allplan_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_revi_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_allplan_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_revi_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_allplan_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_uniq_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_allplan_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_allplan_uniq_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_earth_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_cume_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_earth_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_cume_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_earth_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_revi_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_earth_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_revi_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_earth_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_uniq_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_full_earth_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_full_earth_uniq_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_allplan_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_cume_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_allplan_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_cume_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_allplan_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_revi_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_allplan_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_revi_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_allplan_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_uniq_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_allplan_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_allplan_uniq_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_earth_cume_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_cume_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_earth_cume_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_cume_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_earth_revi_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_revi_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_earth_revi_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_revi_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_earth_uniq_red_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_uniq_red_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_char_part_earth_uniq_union_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_char_part_earth_uniq_union_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_det_allplan_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_cume_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_det_allplan_revi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_revi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_det_allplan_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_allplan_uniq_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_det_earth_cume_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_cume_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_det_earth_revi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_revi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_time_det_earth_uniq_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-yield-time.csv",
            "name": "h_time_det_earth_uniq_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_earth_char_count_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_count_lo_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_earth_char_count_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_count_hi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_earth_char_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_all_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_earth_xchar_all_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_xchar_all_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_earth_char_strict_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-count.csv",
            "name": "h_earth_char_strict_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "ensemble": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "ensemble",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "obsnum": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "obsnum",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "pind": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "pind",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "n_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "n_earth",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "n_success": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "n_success",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "is_success": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "is_success",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "is_deep": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "is_deep",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "is_promo": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "is_promo",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "WA": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "WA",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "dMag": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "dMag",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "phi": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "phi",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "char_SNR": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth-char-list.csv",
            "name": "char_SNR",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_full",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_part": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_part",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_snr": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_snr",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_strict": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_strict",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_tput_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_tput_full",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_tput_strict": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_tput_strict",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_det_alt": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_det_alt",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_det_main": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_det_main",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_population": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_population",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_xchar_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_full",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_xchar_part": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_part",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_xchar_snr": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_snr",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_xchar_tput_full": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xchar_tput_full",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_xdet_alt": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xdet_alt",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_xdet_main": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_xdet_main",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_full_red": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_full_red",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_part_red": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_part_red",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_snr_red": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_snr_red",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_full_union": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_full_union",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_part_union": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_part_union",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "exoE_char_snr_union": {
        "EXOSIMSCSVFile": {
            "file": "reduce-earth.csv",
            "name": "exoE_char_snr_union",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_cand_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_allplan",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_cand_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_earth",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_cand_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_hzone",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_cand_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_cand_star",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det0_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det0_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det0_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det0_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det0_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det1_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det1_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det1_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det1_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det1_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det2_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det2_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det2_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det2_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det2_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det3_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det3_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det3_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det3_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det3_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det4_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det4_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det4_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_det4_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_det4_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_detV_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_detV_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_detV_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_detV_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_detV_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_iwa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_iwa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_iwa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_iwa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_iwa_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_owa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_owa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_owa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_owa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_owa_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_snr_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_snr_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_snr_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_f_snr_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_f_snr_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_fails_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_fails_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_success_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_success_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_allstar_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_allstar_tries_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_cand_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_allplan",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_cand_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_earth",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_cand_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_hzone",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_cand_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_cand_star",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det0_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det0_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det0_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det0_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det0_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det1_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det1_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det1_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det1_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det1_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det2_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det2_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det2_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det2_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det2_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det3_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det3_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det3_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det3_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det3_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det4_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det4_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det4_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_det4_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_det4_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_detV_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_detV_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_detV_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_detV_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_detV_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_iwa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_iwa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_iwa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_iwa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_iwa_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_owa_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_owa_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_owa_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_owa_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_owa_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_snr_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_snr_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_snr_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_f_snr_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_f_snr_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_fails_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_fails_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_success_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_success_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "detfunnel_promo_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-det-funnel.csv",
            "name": "detfunnel_promo_tries_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_lo_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_hi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_char_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_char_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_char_rvplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_char_rvplan_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_det_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_det_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_det_rvplan_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_det_rvplan_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_detp_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_detp_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_count_slew_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-event-counts.csv",
            "name": "h_event_count_slew_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_b0_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b0_duration_lo_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_b0_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b0_duration_hi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_b1_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b1_duration_lo_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_b1_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b1_duration_hi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_b2_duration_lo_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b2_duration_lo_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_b2_duration_hi_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_b2_duration_hi_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_char_b0_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b0_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_char_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b1_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_char_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_char_b2_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_det_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_det_b1_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_det_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_det_b2_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_slew_b0_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b0_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_slew_b1_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b1_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "h_event_slew_b2_duration_mean": {
        "EXOSIMSCSVFile": {
            "file": "reduce-events.csv",
            "name": "h_event_slew_b2_duration_mean",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_allplan",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_chars_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_chars_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_earth",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_hzone",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_star",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_deep_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_deep_tries_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_allplan": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_allplan",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_chars_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_chars_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_earth": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_earth",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_hzone": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_hzone",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_star": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_star",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_allplan_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_allplan_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_allplan_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_allplan_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_earth_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_earth_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_earth_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_earth_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_hzone_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_hzone_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_hzone_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_hzone_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_star_cume": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_star_cume",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "funnel_promo_tries_star_uniq": {
        "EXOSIMSCSVFile": {
            "file": "reduce-funnel.csv",
            "name": "funnel_promo_tries_star_uniq",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": ""
    },
    "Teff": {
        "EXOSIMSInputFile": {
            "file": "json",
            "name": "Teff",
            "unit": "",
            "transform": {
                "type": "none",
                "value": None
            }
        },
        "comment": "EXOSIMS TargetList object attribute"
    },
}
