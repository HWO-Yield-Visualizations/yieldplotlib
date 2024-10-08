"""Centralized key mapping for different file types."""

KEY_MAP = {
    "star_name": {
        "EXOSIMSCSVFile": "star_Name",
        "AYOCSVFile": "HIP",
    },
    "star_L": {
        "EXOSIMSCSVFile": "star_L",
        "AYOCSVFile": "Lstar (Lsun)",
    },
    "star_dist": {
        "EXOSIMSCSVFile": "star_dist",
        "AYOCSVFile": "dist (pc)",
    },
    "star_comp": {
        "EXOSIMSCSVFile": "h_star_char_comp_mean",
        "AYOCSVFile": "Total HZ Completeness",
    },
    "star_spec": {
        "EXOSIMSCSVFile": "star_Spec",
        "AYOCSVFile": "Type",
    },
    "exp_time_det": {
        "EXOSIMSCSVFile": "h_star_det_tInt_mean",
        "AYOCSVFile": "Total BB Imaging Time (days)",
    },
    "exp_time_char": {
        "EXOSIMSCSVFile": "h_star_char_tInt_mean",
        "AYOCSVFile": "Total Spec Char Time (days)",
    },
    # Add more key mappings here
}
