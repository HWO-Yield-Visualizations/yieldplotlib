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
    # Add more key mappings here
}
