"""Resolving-power defaults match EXOSIMS when the input file omits Rs."""

import pytest

from yieldplotlib.load.exosims.exosims_input_file import EXOSIMSInputFile


@pytest.mark.parametrize(
    "inst, top_level, expected",
    [
        ({"name": "imaging_EAC1_BroadbandVisible_500"}, {}, 1.0),
        ({"name": "imager", "Rs": 140}, {}, 1.0),
        ({"name": "spectro_EAC1_IFS_910"}, {}, 50.0),
        ({"name": "spectro_EAC1_IFS_910"}, {"Rs": 70}, 70.0),
        ({"name": "spectro_EAC1_IFS_910", "Rs": 140}, {"Rs": 70}, 140.0),
    ],
)
def test_resolving_power_matches_exosims(inst, top_level, expected):
    """Imagers report Rs = 1; spectrographs fall back to top-level Rs, then 50."""
    node = EXOSIMSInputFile.__new__(EXOSIMSInputFile)
    node.data = top_level
    assert node._resolving_power(inst) == expected
