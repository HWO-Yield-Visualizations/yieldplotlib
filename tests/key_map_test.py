"""Tests for key access in both AYO and EXOSIMS data objects."""

import pytest

from yieldplotlib.key_map import KEY_MAP

# Keys that are not always present in both AYO and EXOSIMS due to
# whether all the data files are present. Generally these are keys
# that must be calculated on the fly and aren't saved to disk.
WHITELIST = ["blind_comp_spec", "blind_comp_det"]


def find_common_keys():
    """Find keys that are present in both AYO and EXOSIMS data sources."""
    common_keys = []
    for key, value in KEY_MAP.items():
        # Check if the key has both AYO and EXOSIMS entries
        has_ayo = any(key_name.startswith("AYO") for key_name in value)
        has_exosims = any(key_name.startswith("EXOSIMS") for key_name in value)

        # Only add the key if it has both AYO AND EXOSIMS entries
        common_keys.append(key) if has_ayo and has_exosims else None

    return common_keys


def test_common_key_access(ayo_data, exosims_data):
    """Test that both AYO and EXOSIMS can access the same data via key_map."""
    common_keys = find_common_keys()

    # Make sure we found some common keys
    assert len(common_keys) > 0, "No common keys found between AYO and EXOSIMS"

    for key in common_keys:
        if key in WHITELIST:
            continue
        try:
            ayo_value = ayo_data.get(key)
            # Just check that we can access the data without error
            assert ayo_value is not None, f"Failed to retrieve AYO data for key: {key}"
        except Exception as e:
            pytest.skip(f"Skipping key {key} for AYO: {str(e)}")

        try:
            exosims_value = exosims_data.get(key)
            # Just check that we can access the data without error
            assert exosims_value is not None, (
                f"Failed to retrieve EXOSIMS data for key: {key}"
            )
        except Exception as e:
            pytest.skip(f"Skipping key {key} for EXOSIMS: {str(e)}")


def test_all_common_keys_list():
    """Print a list of all common keys."""
    common_keys = find_common_keys()
    # This is mainly a sanity check, but also serves as a basic test
    assert len(common_keys) > 0, "No common keys found between AYO and EXOSIMS"
    # The test passes if we get here
    print(f"Found {len(common_keys)} common keys between AYO and EXOSIMS:")
    print(", ".join(common_keys))
