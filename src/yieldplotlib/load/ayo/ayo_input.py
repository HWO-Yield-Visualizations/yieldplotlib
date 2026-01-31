"""Node for handling input .ayo files."""

import json
from pathlib import Path

import astropy.units as u
import numpy as np
import pyparsing as pp
from lod_unit import lod
from yippy.coronagraph import Coronagraph

from yieldplotlib.core.file_nodes import FileNode
from yieldplotlib.logger import logger

# Define 'read' as a dimensionless unit
read = u.def_unit("read")
u.add_enabled_units([read])

# Define zodis as a dimensionless unit
zodis = u.def_unit("zodis")
u.add_enabled_units([zodis])


class AYOInputFile(FileNode):
    """Node for handling AYO input files using PyParsing."""

    def __init__(self, file_path: Path):
        """Initialize the AYOInputFile node with the file path."""
        super().__init__(file_path)
        self.data = {}
        self.parse()
        self.is_input = True

    def load(self):
        """Load the text file into memory."""
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.raw_data = f.read()
        logger.info(f"Loaded AYO input file: {self.file_path}")

    def _get(self, key: str, **kwargs):
        """Return the data associated with the key."""
        return self.data.get(key, None)

    def parse(self):
        """Parse the AYO input file and populate the self.data dictionary."""
        # Define a unit as a word composed of alphabetic characters and underscores,
        # possibly combined with slashes for compound units
        simple_unit = pp.Word(pp.alphas, pp.alphanums + "_")
        compound_unit = pp.Combine(simple_unit + pp.ZeroOrMore("/" + simple_unit))

        # Unit can be either a compound unit or a simple unit
        unit = compound_unit("unit")

        # Define an optional exponent, e.g., ^-1, ^2
        exponent = pp.Suppress("^") + pp.Regex(r"[+-]?\d+").setParseAction(
            lambda t: int(t[0])
        )

        # Define a unit with an optional exponent
        unit_with_exp = pp.Group(unit + pp.Optional(exponent, default=1)("degree"))

        # Define grammar for a single key-value pair with type identifier
        identifier = pp.Word(pp.alphas + "_", pp.alphanums + "_").setName("identifier")

        # Define number (integer or float)
        number = pp.common.number().setName("number")

        # Define string (single or double quoted)
        string = pp.QuotedString("'", escChar="\\") | pp.QuotedString('"', escChar="\\")

        # Define array
        array = (
            pp.Group(
                pp.Suppress("[")
                + pp.Optional(pp.delimitedList(number | string, delim=","))
                + pp.Suppress("]")
            )
            .setName("array")
            .setParseAction(self._convert_array)
        )

        # Define parameter reference (used in expressions)
        param_ref = identifier.copy().setName("param_ref")

        # Define expression parts - handle addition, subtraction,
        # multiplication, division
        expr_term = number | param_ref

        # Simple expressions (value op value)
        simple_expr = (expr_term + pp.oneOf("+ - * /") + expr_term).setName(
            "simple_expr"
        )

        # Define a post-processing function for mathematical expressions
        def process_expression(tokens):
            """Process a mathematical expression with parameter references."""
            if len(tokens) == 3:  # It's an expression like a + b or a - b
                left, op, right = tokens

                # If the right side is a parameter reference, look it up
                if isinstance(right, str) and right in self.data:
                    right_val = self.data[right]
                else:
                    right_val = right

                # If the left side is a parameter reference, look it up
                if isinstance(left, str) and left in self.data:
                    left_val = self.data[left]
                else:
                    left_val = left

                # Perform the operation
                if op == "+":
                    return left_val + right_val
                elif op == "-":
                    return left_val - right_val
                elif op == "*":
                    return left_val * right_val
                elif op == "/":
                    return left_val / right_val

            return tokens[0]  # Not an expression we recognize

        # Define the expression and set its parse action
        expression = simple_expr.setParseAction(process_expression)

        # Define type identifier in curly braces
        type_literal = (
            pp.Suppress("{")
            + pp.Word(pp.alphas).setResultsName("type")
            + pp.SkipTo(pp.Suppress("}"))
        )

        # Unit identifier in parentheses
        unit_literal = (
            pp.Suppress("(")
            + pp.OneOrMore(unit_with_exp)
            .setResultsName("units")
            .setParseAction(self._convert_unit)
            + pp.Suppress(") ")
        )

        # Define all possible value types with priorities (try more specific
        # patterns first)
        value_types = expression | array | string | number | param_ref

        # Define key-value pair with type, optional unit, and optional comments
        key_value = (
            identifier.setResultsName("key")
            + pp.Suppress("=")
            + value_types.setResultsName("value")
            + pp.Optional(pp.Suppress(";"))  # Semicolon is optional
            + pp.Optional(unit_literal)
            + pp.Optional(pp.SkipTo("{").setResultsName("comment_before_type"))
            + pp.Optional(type_literal)
            + pp.Optional(pp.SkipTo(pp.lineEnd()).setResultsName("comment_after_type"))
        )

        # Split the raw data into individual lines
        input_file_lines = self.raw_data.split("\n")

        for line_number, line in enumerate(input_file_lines, start=1):
            line = line.strip()

            # Skip empty lines and lines starting with ';' or '#'
            if not line or line.startswith(";") or line.startswith("#"):
                continue

            try:
                # Parse the line using the defined parser
                parsed = key_value.parseString(line, parseAll=True)

                # Extract key, value, and type from the parsed result
                key = parsed["key"]
                type_ = parsed.get("type", "string").lower()
                value = parsed["value"][0]
                if "units" in parsed:
                    unit = parsed["units"]
                    value *= unit

                # Store the value in self.data
                self.data[key] = value
                logger.debug(f"Parsed {type_}: {key} = {value}")
            except pp.ParseException as e:
                logger.warning(f"Failed to parse line {line_number}: {line}")
                logger.warning(f"Error: {e}")
                continue

        # After parsing, set expected_keys based on the input keys
        self.expected_keys = list(self.data.keys())
        logger.info(f"Successfully parsed {len(self.data)} input parameters.")

    def _convert_array(self, tokens):
        """Convert parsed array tokens to a Python list."""
        array = tokens[0].asList()
        return np.array(array)

    def _convert_unit(self, parsed_unit):
        """Convert parsed unit string to the appropriate astropy unit."""
        # get the unit from the ParseResult object
        _map = {
            "years": u.yr,
            "l/D": lod,
            "lambda/D": lod,
            "mags": u.mag,
            "microns": u.um,
            "counts": u.count,
            "photon_count": u.photon,
            "read": read,
            "degrees": u.deg,
        }
        _whitelist = []
        final_unit = None
        n_units = 0
        for current_unit in parsed_unit:
            current_unit_str = current_unit["unit"]
            if current_unit_str in _whitelist:
                continue
            if current_unit_str in _map.keys():
                # Get the unit from the predefined map
                _u = _map[current_unit_str]
            else:
                # Parse as an astropy unit
                _u = u.Unit(current_unit_str)

            # Apply the exponent
            current_unit_degree = current_unit["degree"]
            # Apply exponent and include the unit in the final unit
            if n_units == 0:
                final_unit = _u**current_unit_degree
            else:
                final_unit *= _u**current_unit_degree
            n_units += 1

        return final_unit

    def export_exosims(
        self,
        output_path: str,
        base_file: Path | str | None = None,
        detection_wavelength_nm: float | None = None,
        characterization_wavelength_nm: float | None = None,
        **kwargs,
    ):
        """Export the AYO input to an EXOSIMS JSON file.

        Args:
            output_path:
                Path to write the output JSON file.
            base_file:
                Optional path to a base EXOSIMS JSON file. If provided, AYO
                parameters will overwrite equivalent parameters in the base file,
                and all other parameters will be preserved.
            detection_wavelength_nm:
                Wavelength in nanometers to use for detection mode. The closest
                wavelength in the lambda array will be selected. If None, uses
                the middle wavelength (default).
            characterization_wavelength_nm:
                Wavelength in nanometers to use for characterization mode. The
                closest wavelength in the sc_lambda array will be selected. If
                None, uses the middle wavelength (default).
            **kwargs:
                Additional keyword arguments to include in the output JSON.
                These will overwrite any existing values. Useful for setting
                paths like cachedir, e.g.:
                    cachedir="$HOME/.EXOSIMS/2025/Natasha_JATIS"
        """

        # Helper to round floats to avoid repeating decimals
        def round_float(val, decimals=6):
            """Round float values to specified decimal places."""
            if val is None:
                return None
            if isinstance(val, (int, float)):
                return round(float(val), decimals)
            if isinstance(val, (list, np.ndarray)):
                return [round_float(v, decimals) for v in val]
            return val

        # Helper to safely get values with units or defaults
        def get_val(key, unit=None, default=None):
            val = self.data.get(key)
            if val is None:
                return default
            # Check if val is a Quantity (has .unit or .value)
            if hasattr(val, "value"):
                if unit:
                    try:
                        return val.to(unit).value
                    except u.UnitConversionError:
                        return val.value
                return val.value
            return val

        # Helper for arrays (return value if scalar, or array item)
        def get_array_val(key, idx, default=None, unit=None):
            val = self.data.get(key)
            if val is None:
                return default

            # If Quantity, convert to target unit if specified
            if hasattr(val, "value"):
                if unit is not None:
                    try:
                        val = val.to(unit)
                    except u.UnitConversionError:
                        pass  # Keep original if conversion fails
                v = val.value
            else:
                v = val

            if isinstance(v, (list, np.ndarray)):
                if idx < len(v):
                    return v[idx]
                # Warn when index is out of bounds - likely array length mismatch
                raise ValueError(
                    f"Index {idx} out of bounds for '{key}' (length {len(v)}). "
                    f"Check that wavelength arrays have matching lengths."
                )
            return v  # Scalar

        # Load base file if provided
        if base_file is not None:
            base_path = Path(base_file)
            if not base_path.exists():
                raise FileNotFoundError(f"Base EXOSIMS file not found: {base_path}")
            with open(base_path, "r") as f:
                out = json.load(f)
            logger.info(f"Loaded base EXOSIMS file: {base_path}")
        else:
            # Initialize with defaults if no base file
            out = {
                "missionLife": 5.0,
                "missionStart": 60634,
                "pupilDiam": 4.0,
                "koAngles_Sun": [45, 135],
                "modules": {
                    "PlanetPopulation": "AlbedoByRadiusDulzPlavchan",
                    "StarCatalog": "HPIC",
                    "OpticalSystem": "Nemati",
                    "ZodiacalLight": "Mennesson",
                    "BackgroundSources": "GalaxiesFaintStars",
                    "PlanetPhysicalModel": "Forecaster",
                    "Observatory": "WFIRSTObservatoryL2",
                    "TimeKeeping": " ",
                    "PostProcessing": " ",
                    "Completeness": "BrownCompleteness",
                    "TargetList": " ",
                    "SimulatedUniverse": "DulzPlavchanUniverseEarthsOnly",
                    "SurveySimulation": "coroOnlyScheduler",
                    "SurveyEnsemble": "EXOSIMS_local.IPClusterEnsembleJPL2",
                },
                "scienceInstruments": [],
                "starlightSuppressionSystems": [],
                "observingModes": [],
            }

        # Set settlingTime to 0 since all overhead is handled by ohTime in the system
        # AYO's toverhead_fixed includes all overhead (slew + settle + initial
        # dark hole digging)
        out["settlingTime"] = 0.0

        # Extract AYO parameters and overwrite base values
        D_m = get_val("D", u.m, None)
        if D_m is not None:
            out["pupilDiam"] = round_float(float(D_m))

        # Get nchannels for multi-channel coronagraph simulation.
        # nchannels splits light into identical channels - EXOSIMS doesn't have
        # a direct analog, so we approximate by:
        # 1. Multiplying BW by nchannels (increased signal from combined channels)
        # 2. Multiplying lenslSamp by sqrt(nchannels) (since lenslSamp is squared
        #    in EXOSIMS to get Npix, this gives Npix proportional to nchannels)
        nchannels = get_val("nchannels", None, 1)
        if nchannels is None:
            nchannels = 1
        else:
            nchannels = int(nchannels)
        if nchannels > 1:
            logger.info(
                f"Applying nchannels={nchannels} to detection only: "
                f"optics *= {nchannels}, "
                f"lenslSamp *= sqrt({nchannels}) = {np.sqrt(nchannels):.4f}"
            )

        mission_life_yr = get_val("mission_lifetime", u.yr, None)
        if mission_life_yr is not None:
            out["missionLife"] = round_float(float(mission_life_yr))

        # AYO pitch is [min, max] from Sun
        # Will be set in starlightSuppressionSystems later
        ko_sun = self.data.get("pitch")
        if ko_sun is not None:
            if hasattr(ko_sun, "unit"):
                ko_sun = ko_sun.to(u.deg).value.tolist()
            elif isinstance(ko_sun, np.ndarray):
                ko_sun = ko_sun.tolist()
        else:
            ko_sun = None

        # Handle missionPortion
        total_time = get_val("total_survey_time", u.yr, None)
        mission_life_yr = out.get("missionLife", 5.0)
        if total_time is not None and mission_life_yr > 0:
            out["missionPortion"] = round_float(float(total_time / mission_life_yr))

        # Map nexozodis to fixed_nEZ_val
        nexozodis = get_val("nexozodis", zodis, None)
        if nexozodis is not None:
            # nexozodis is in zodis (dimensionless unit), convert to float
            if hasattr(nexozodis, "value"):
                out["fixed_nEZ_val"] = round_float(float(nexozodis.value))
            else:
                out["fixed_nEZ_val"] = round_float(float(nexozodis))

        # Map noisefloor_PPF to ppFact and ppFact_char (inverse relationship)
        noisefloor_PPF = get_val("noisefloor_PPF", None, None)
        if noisefloor_PPF is not None:
            pp_fact_val = round_float(1.0 / float(noisefloor_PPF))
            out["ppFact"] = pp_fact_val
            out["ppFact_char"] = pp_fact_val
            logger.info(
                f"Set ppFact and ppFact_char to {pp_fact_val} "
                f"(from noisefloor_PPF={noisefloor_PPF})"
            )

        # Update optional_filters based on AYO target list cuts
        # Initialize optional_filters if not present
        if "optional_filters" not in out:
            out["optional_filters"] = {}

        # Update vmag_filter with target_vmag_cut
        target_vmag_cut = get_val("target_vmag_cut", None, None)
        if target_vmag_cut is not None:
            # Get existing vmag_range from base file if present,
            # otherwise use default min
            existing_vmag_filter = out["optional_filters"].get("vmag_filter", {})
            existing_params = existing_vmag_filter.get("params", {})
            existing_range = existing_params.get("vmag_range", [0, 15])
            vmag_min = existing_range[0] if isinstance(existing_range, list) else 2

            out["optional_filters"]["vmag_filter"] = {
                "enabled": True,
                "params": {
                    "vmag_range": [
                        round_float(vmag_min),
                        round_float(float(target_vmag_cut)),
                    ]
                },
            }
            logger.info(
                f"Updated vmag_filter with range [{vmag_min:.1f}, "
                f"{target_vmag_cut:.1f}]"
            )

        # Update distance_filter with target_distance_cut
        target_distance_cut = get_val("target_distance_cut", u.pc, None)
        if target_distance_cut is not None:
            out["optional_filters"]["distance_filter"] = {
                "enabled": True,
                "params": {"max_distance": round_float(float(target_distance_cut))},
            }
            logger.info(
                f"Updated distance_filter with max_distance = "
                f"{target_distance_cut:.1f} pc"
            )

        # Load coronagraph using yippy and generate starlightSuppressionSystem
        coronagraph_path = self.data.get("coronagraph1")

        # Initialize coronagraph design bandwidth (will be set if coronagraph loaded)
        coro_design_bw = None

        if coronagraph_path:
            # Remove quotes if present (from string parsing)
            if isinstance(coronagraph_path, str):
                coronagraph_path = coronagraph_path.strip("'\"")

            # Try to find the coronagraph directory
            # First try as absolute path, then relative to AYO file directory
            coro_path = Path(coronagraph_path)
            if not coro_path.is_absolute():
                # Try relative to AYO file's directory
                ayo_dir = self.file_path.parent
                coro_path = ayo_dir / coronagraph_path
                # If still not found, try as-is (might be in a standard location)
                if not coro_path.exists():
                    coro_path = Path(coronagraph_path)

            if coro_path.exists():
                logger.info(f"Loading coronagraph from: {coro_path}")
                # Load coronagraph with yippy
                coro = Coronagraph(coro_path, use_jax=False)

                # Extract coronagraph's design fractional bandwidth from header
                # AYO uses min(1/SR, coro_design_bw) as the effective bandwidth
                if (
                    coro.header.minlam is not None
                    and coro.header.maxlam is not None
                    and coro.header.lambda0 is not None
                ):
                    coro_design_bw = (
                        (
                            (coro.header.maxlam - coro.header.minlam)
                            / coro.header.lambda0
                        )
                        .decompose()
                        .value
                    )
                    logger.info(
                        f"Coronagraph design bandwidth: {coro_design_bw:.4f} "
                        f"(from MINLAM={coro.header.minlam}, "
                        f"MAXLAM={coro.header.maxlam}, LAMBDA={coro.header.lambda0})"
                    )

                # Generate EXOSIMS files and get system info
                # Use AYO parameters if available, otherwise defaults
                aperture_radius = get_val("photap_rad", lod, 0.7)
                if aperture_radius is None:
                    aperture_radius = 0.7
                else:
                    aperture_radius = aperture_radius

                # Get IWA/OWA from AYO if available, otherwise use defaults
                iwa_lod = get_val("IWA", lod, None)
                owa_lod = get_val("OWA", lod, None)

                # Generate EXOSIMS format files
                exosims_specs = coro.to_exosims(
                    aperture_radius_lod=aperture_radius,
                    fit_gaussian_for_core_area=False,
                    use_phot_aperture_as_min=False,
                    units="LAMBDA/D",
                )

                # Get the system from the generated specs
                if exosims_specs.get("starlightSuppressionSystems"):
                    syst = exosims_specs["starlightSuppressionSystems"][0].copy()

                    # Convert relative FITS file paths to absolute paths
                    exosims_dir = Path(coro_path, "exosims")
                    fits_files = ["occ_trans", "core_thruput", "core_mean_intensity"]
                    for fits_key in fits_files:
                        if fits_key in syst and syst[fits_key]:
                            # If it's a relative path, make it absolute
                            fits_path = Path(syst[fits_key])
                            if not fits_path.is_absolute():
                                fits_path = exosims_dir / fits_path
                            syst[fits_key] = str(fits_path.resolve())

                    # Override with AYO parameters if specified
                    contrast = get_val("raw_contrast_floor", None, None)
                    if contrast is not None:
                        syst["core_contrast"] = float(contrast)

                    overhead = get_val("toverhead_fixed", u.d, None)
                    if overhead is not None:
                        syst["ohTime"] = round_float(float(overhead))

                    # Override IWA/OWA from AYO if specified
                    # AYO IWA/OWA are in LAMBDA/D, same as yippy output
                    if iwa_lod is not None:
                        if hasattr(iwa_lod, "value"):
                            syst["IWA"] = round_float(float(iwa_lod.to(lod).value))
                        else:
                            syst["IWA"] = round_float(float(iwa_lod))
                    if owa_lod is not None:
                        if hasattr(owa_lod, "value"):
                            syst["OWA"] = round_float(float(owa_lod.to(lod).value))
                        else:
                            syst["OWA"] = round_float(float(owa_lod))

                    # Round other float values in the system
                    for key in ["lam", "deltaLam", "BW", "core_area"]:
                        if key in syst and syst[key] is not None:
                            syst[key] = round_float(syst[key])

                    # Update pupilDiam from coronagraph if not set by AYO
                    if D_m is None and "pupilDiam" in exosims_specs:
                        out["pupilDiam"] = round_float(exosims_specs["pupilDiam"])

                    # Extract obscurFac and shapeFac from exosims_specs
                    if "obscurFac" in exosims_specs:
                        out["obscurFac"] = round_float(exosims_specs["obscurFac"])
                    if "shapeFac" in exosims_specs:
                        out["shapeFac"] = round_float(exosims_specs["shapeFac"])

                    # Set koAngles_Sun from AYO pitch, preserve other koAngles
                    if ko_sun is not None:
                        syst["koAngles_Sun"] = [round_float(x) for x in ko_sun]
                    # Preserve other koAngles if they exist in base file
                    if (
                        "starlightSuppressionSystems" in out
                        and len(out["starlightSuppressionSystems"]) > 0
                    ):
                        base_syst = out["starlightSuppressionSystems"][0]
                        ko_keys = [
                            "koAngles_Small",
                            "koAngles_Moon",
                            "koAngles_Earth",
                        ]
                        for ko_key in ko_keys:
                            if ko_key in base_syst:
                                syst[ko_key] = base_syst[ko_key]

                    # Set BW in starlightSuppressionSystem from detection wavelength SR
                    # Calculate BW from detection wavelength's spectral resolution
                    lams = self.data.get("lambda")
                    if lams is not None:
                        if hasattr(lams, "unit"):
                            lams_nm = lams.to(u.nm).value
                        else:
                            lams_nm = np.array(lams) * 1000
                        if not isinstance(lams_nm, (list, np.ndarray)):
                            lams_nm = [lams_nm]
                        lams_nm = np.array(lams_nm)

                        # Use same wavelength selection logic as for detection mode
                        if detection_wavelength_nm is None:
                            det_idx = len(lams_nm) // 2
                        else:
                            det_idx = int(
                                np.argmin(np.abs(lams_nm - detection_wavelength_nm))
                            )

                        det_sr = get_array_val("SR", det_idx, 5.0)
                        sr_bw = 1.0 / float(det_sr) if det_sr > 0 else 0.2
                        # Take minimum of 1/SR and coronagraph design bandwidth
                        if coro_design_bw is not None:
                            base_bw = min(sr_bw, coro_design_bw)
                            if base_bw < sr_bw:
                                logger.info(
                                    f"BW limited by coronagraph design: "
                                    f"{base_bw:.4f} < 1/SR={sr_bw:.4f}"
                                )
                        else:
                            base_bw = sr_bw
                        # DO NOT multiply BW by nchannels. Keep it physical.
                        syst["BW"] = round_float(base_bw)
                        # Remove deltaLam so EXOSIMS calculates it from our BW
                        # (EXOSIMS recalculates BW = deltaLam/lam, so if deltaLam
                        # is present, our BW would be ignored)
                        syst.pop("deltaLam", None)
                    elif "BW" not in syst:
                        # Default if no detection wavelengths
                        default_bw = 0.2
                        if coro_design_bw is not None:
                            default_bw = min(default_bw, coro_design_bw)
                        # DO NOT multiply BW by nchannels. Keep it physical.
                        syst["BW"] = round_float(default_bw)
                        syst.pop("deltaLam", None)

                    # Remove core_contrast if core_mean_intensity is set
                    # (EXOSIMS uses one or the other, not both)
                    if syst.get("core_mean_intensity"):
                        syst.pop("core_contrast", None)

                    # Replace or append the system
                    if "starlightSuppressionSystems" not in out:
                        out["starlightSuppressionSystems"] = []
                    if len(out["starlightSuppressionSystems"]) == 0:
                        out["starlightSuppressionSystems"].append(syst)
                    else:
                        out["starlightSuppressionSystems"][0] = syst
                else:
                    logger.warning(
                        "No starlightSuppressionSystems found in coronagraph specs"
                    )
                # except Exception as e:
                #     logger.warning(
                #         f"Failed to load coronagraph from {coro_path}: {e}. "
                #         "Falling back to manual construction."
                #     )
                #     # Fall through to manual construction
                #     coronagraph_path = None

        # Fallback: Manual construction if coronagraph not found or failed to load
        if (
            not coronagraph_path
            or "starlightSuppressionSystems" not in out
            or len(out["starlightSuppressionSystems"]) == 0
        ):
            logger.info("Using manual starlightSuppressionSystem construction")
            # Get or create starlightSuppressionSystems
            if "starlightSuppressionSystems" not in out:
                out["starlightSuppressionSystems"] = []
                syst = {}
            elif len(out["starlightSuppressionSystems"]) == 0:
                # Create new system if list is empty
                syst = {}
            else:
                # Update first system with AYO parameters
                syst = out["starlightSuppressionSystems"][0].copy()

            # Convert AYO IWA (L/D) to EXOSIMS
            # (assume arcsec for safety or standard input)
            # Using a reference lambda of 500nm
            ref_lam_m = 500e-9
            D_m = out.get("pupilDiam", 4.0)
            iwa_lod = get_val("IWA", lod, None)
            owa_lod = get_val("OWA", lod, None)

            if iwa_lod is not None or owa_lod is not None:
                # Convert to arcsec: IWA_as = IWA_lod * (lam/D)_as
                # (lam/D)_rad = lam/D. (lam/D)_as = 206265 * lam/D
                lod_to_as = 206265.0 * (ref_lam_m / D_m)

                if iwa_lod is not None:
                    syst["IWA"] = round_float(float(iwa_lod * lod_to_as))
                if owa_lod is not None:
                    syst["OWA"] = round_float(float(owa_lod * lod_to_as))

            # Update system parameters from AYO
            contrast = get_val("raw_contrast_floor", None, None)
            if contrast is not None:
                syst["core_contrast"] = round_float(float(contrast))

            overhead = get_val("toverhead_fixed", u.d, None)
            if overhead is not None:
                syst["ohTime"] = round_float(float(overhead))

            # Set default system name if not present
            if "name" not in syst:
                syst["name"] = "AYO_Coronagraph"
            if "lam" not in syst:
                syst["lam"] = round_float(500)  # nm
            # Set BW from detection wavelength SR if available
            if "BW" not in syst:
                lams = self.data.get("lambda")
                if lams is not None:
                    if hasattr(lams, "unit"):
                        lams_nm = lams.to(u.nm).value
                    else:
                        lams_nm = np.array(lams) * 1000
                    if not isinstance(lams_nm, (list, np.ndarray)):
                        lams_nm = [lams_nm]
                    lams_nm = np.array(lams_nm)

                    # Use same wavelength selection logic as for detection mode
                    if detection_wavelength_nm is None:
                        det_idx = len(lams_nm) // 2
                    else:
                        det_idx = int(
                            np.argmin(np.abs(lams_nm - detection_wavelength_nm))
                        )

                    det_sr = get_array_val("SR", det_idx, 5.0)
                    sr_bw = 1.0 / float(det_sr) if det_sr > 0 else 0.2
                    # Take minimum of 1/SR and coronagraph design bandwidth
                    if coro_design_bw is not None:
                        base_bw = min(sr_bw, coro_design_bw)
                        if base_bw < sr_bw:
                            logger.info(
                                f"BW limited by coronagraph design: "
                                f"{base_bw:.4f} < 1/SR={sr_bw:.4f}"
                            )
                    else:
                        base_bw = sr_bw
                    # DO NOT multiply BW by nchannels. Keep it physical.
                    syst["BW"] = round_float(base_bw)
                    # Remove deltaLam so EXOSIMS calculates it from our BW
                    syst.pop("deltaLam", None)
                else:
                    default_bw = 0.2
                    if coro_design_bw is not None:
                        default_bw = min(default_bw, coro_design_bw)
                    # DO NOT multiply BW by nchannels. Keep it physical.
                    syst["BW"] = round_float(default_bw)
                    syst.pop("deltaLam", None)

            # Set koAngles_Sun from AYO pitch, preserve other koAngles from base
            if ko_sun is not None:
                syst["koAngles_Sun"] = [round_float(x) for x in ko_sun]
            # Preserve other koAngles if they exist in base file
            if (
                "starlightSuppressionSystems" in out
                and len(out["starlightSuppressionSystems"]) > 0
            ):
                base_syst = out["starlightSuppressionSystems"][0]
                for ko_key in ["koAngles_Small", "koAngles_Moon", "koAngles_Earth"]:
                    if ko_key in base_syst:
                        syst[ko_key] = base_syst[ko_key]

            # Remove core_contrast if core_mean_intensity is set
            # (EXOSIMS uses one or the other, not both)
            if syst.get("core_mean_intensity"):
                syst.pop("core_contrast", None)

            # Replace or append the system
            if len(out["starlightSuppressionSystems"]) == 0:
                out["starlightSuppressionSystems"].append(syst)
            else:
                out["starlightSuppressionSystems"][0] = syst

        # Get system name for use in modes
        syst_name = "AYO_Coronagraph"
        if (
            out.get("starlightSuppressionSystems")
            and len(out["starlightSuppressionSystems"]) > 0
        ):
            syst_name = out["starlightSuppressionSystems"][0].get("name", syst_name)

        # Get or create scienceInstruments and observingModes
        if "scienceInstruments" not in out:
            out["scienceInstruments"] = []
        if "observingModes" not in out:
            out["observingModes"] = []

        # Clear existing instruments and modes if AYO defines them
        instruments = []
        modes = []

        # Get Tcontam (contamination throughput factor) - applies to both
        # detection and characterization
        Tcontam = get_val("Tcontam", None, 1.0)
        if Tcontam is None:
            Tcontam = 1.0
        else:
            Tcontam = float(Tcontam)
            logger.info(f"Applying Tcontam={Tcontam:.6f} to optics throughput")

        # SAFEGUARD: Check for potential double-counting of throughput factors
        # If the base file has syst['optics'] set AND AYO has Tcontam, this would
        # cause the contamination throughput to be applied twice:
        # - Once via Tcontam being multiplied into inst['optics']
        # - Once via syst['optics'] in the base file
        # EXOSIMS computes: attenuation = inst['optics'] * syst['optics']
        if Tcontam != 1.0:
            for syst in out.get("starlightSuppressionSystems", []):
                if "optics" in syst:
                    syst_optics = syst["optics"]
                    syst_name = syst.get("name", "unnamed")
                    logger.warning(
                        f"CONFLICT DETECTED: Base file has "
                        f"syst['{syst_name}']['optics']={syst_optics} AND AYO has "
                        f"Tcontam={Tcontam}. Would cause double-counting. "
                        f"Removing syst['optics']."
                    )
                    del syst["optics"]

        # Process Detection
        lams = self.data.get("lambda")
        if lams is not None:
            # Get values in nm
            if hasattr(lams, "unit"):
                lams_nm = lams.to(u.nm).value
            else:
                lams_nm = (
                    np.array(lams) * 1000
                )  # Assume microns if no unit, convert to nm

            if not isinstance(lams_nm, (list, np.ndarray)):
                lams_nm = [lams_nm]
            lams_nm = np.array(lams_nm)

            # Select which wavelength to use
            if detection_wavelength_nm is None:
                # Default: use middle wavelength
                i = len(lams_nm) // 2
            else:
                # Find closest wavelength to the requested value
                i = int(np.argmin(np.abs(lams_nm - detection_wavelength_nm)))
                logger.info(
                    f"Selected detection wavelength {lams_nm[i]:.1f} nm "
                    f"(closest to requested {detection_wavelength_nm:.1f} nm)"
                )

            # Create Mode for selected wavelength only
            lam = lams_nm[i]
            sr = get_array_val("SR", i, 5.0)
            snr = get_array_val("SNR", i, 5.0)

            # Create Detection Instrument using values at selected wavelength index
            # Format: imaging_{wavelength_nm}_ayo
            lam_int = int(round(float(lam)))
            inst_det_name = f"imaging_{lam_int}_ayo"

            # --- PIXEL MATH CORRECTION ---
            # EXOSIMS squares lenslSamp to get Npix. AYO defines Npix directly.
            # We want lenslSamp^2 = base * nchannels
            base_npix_det = float(get_array_val("det_npix_multiplier", i, 1.0))
            corrected_lenslSamp_det = np.sqrt(base_npix_det * nchannels)

            # --- THROUGHPUT & CHANNELS CORRECTION ---
            # Combine Toptical, dQE, nchannels, and Tcontam into one
            # "Effective Optics" term.
            # - dQE scales Signal & Noise Floor (matching AYO behavior)
            # - nchannels sums the signal from multiple detectors
            # - Tcontam accounts for contamination throughput losses
            dQE_det = float(get_array_val("det_dQE", i, 0.75))
            Topt_det = float(get_array_val("Toptical", i, 0.5))
            effective_optics_det = Topt_det * dQE_det * nchannels * Tcontam

            inst_det = {
                "name": inst_det_name,
                "pixelScale": round_float(
                    float(get_val("det_pixscale_mas", None, 10.0) / 1000.0)
                ),  # as
                "idark": round_float(float(get_array_val("det_DC", i, 0))),
                "CIC": round_float(float(get_array_val("det_CIC", i, 1e-3))),
                "sread": round_float(float(get_array_val("det_RN", i, 0.0))),
                "texp": round_float(float(get_array_val("det_tread", i, 100.0, u.s))),
                "texp_flag": False,
                "QE": round_float(float(get_array_val("det_QE", i, 0.9))),
                "optics": round_float(effective_optics_det),  # Handle dQE and nchannels
                "PCeff": 1.0,  # Set to 1.0 to avoid double counting
                "lenslSamp": round_float(corrected_lenslSamp_det),
            }
            instruments.append(inst_det)

            mode = {
                "instName": inst_det_name,
                "systName": syst_name,
                "detectionMode": True,
                "lam": round_float(float(lam)),
                "SNR": round_float(float(snr)),
            }
            modes.append(mode)

        # Process Characterization
        sc_lams = self.data.get("sc_lambda")
        if sc_lams is not None:
            if hasattr(sc_lams, "unit"):
                sc_lams_nm = sc_lams.to(u.nm).value
            else:
                sc_lams_nm = np.array(sc_lams) * 1000

            if not isinstance(sc_lams_nm, (list, np.ndarray)):
                sc_lams_nm = [sc_lams_nm]
            sc_lams_nm = np.array(sc_lams_nm)

            # Select which wavelength to use
            if characterization_wavelength_nm is None:
                # Default: use middle wavelength
                i = len(sc_lams_nm) // 2
            else:
                # Find closest wavelength to the requested value
                i = int(np.argmin(np.abs(sc_lams_nm - characterization_wavelength_nm)))
                logger.info(
                    f"Selected characterization wavelength {sc_lams_nm[i]:.1f} nm "
                    f"(closest to requested {characterization_wavelength_nm:.1f} nm)"
                )

            # Get spectral resolution for characterization instrument
            lam = sc_lams_nm[i]
            sr = get_array_val("sc_SR", i, 5.0)
            snr = get_array_val("sc_SNR", i, 5.0)

            # Create Characterization Instrument using values at selected wavelength
            # Format: spectro_{wavelength_nm}_ayo
            lam_int = int(round(float(lam)))
            inst_char_name = f"spectro_{lam_int}_ayo"

            # --- PIXEL MATH CORRECTION ---
            # EXOSIMS squares lenslSamp to get Npix. AYO defines Npix directly.
            # We want lenslSamp^2 = base (nchannels only affects detection)
            base_npix_char = float(get_array_val("sc_det_npix_multiplier", i, 1.0))
            corrected_lenslSamp_char = np.sqrt(base_npix_char)

            # --- THROUGHPUT & CHANNELS CORRECTION ---
            # Combine Toptical, dQE, and Tcontam into one "Effective Optics" term.
            # - dQE scales Signal & Noise Floor (matching AYO behavior)
            # - Tcontam accounts for contamination throughput losses
            # - nchannels only affects detection, not characterization
            dQE_char = float(get_array_val("sc_det_dQE", i, 0.75))
            Topt_char = float(get_array_val("sc_Toptical", i, 0.5))
            effective_optics_char = Topt_char * dQE_char * Tcontam

            inst_char = {
                "name": inst_char_name,
                "pixelScale": round_float(
                    float(get_val("sc_det_pixscale_mas", None, 10.0) / 1000.0)
                ),
                "idark": round_float(float(get_array_val("sc_det_DC", i, 0))),
                "CIC": round_float(float(get_array_val("sc_det_CIC", i, 1e-3))),
                "sread": round_float(float(get_array_val("sc_det_RN", i, 0.0))),
                "texp": round_float(
                    float(get_array_val("sc_det_tread", i, 100.0, u.s))
                ),
                "texp_flag": False,
                "QE": round_float(float(get_array_val("sc_det_QE", i, 0.9))),
                "optics": round_float(effective_optics_char),  # dQE and nchannels
                "PCeff": 1.0,  # Set to 1.0 to avoid double counting
                "Rs": round_float(float(sr)),
                "lenslSamp": round_float(corrected_lenslSamp_char),
            }
            instruments.append(inst_char)

            # Create Mode for selected wavelength only
            mode = {
                "instName": inst_char_name,
                "systName": syst_name,
                "detectionMode": False,
                "lam": round_float(float(lam)),
                "SNR": round_float(float(snr)),
            }
            modes.append(mode)

        # Only replace instruments/modes if AYO defines them
        if instruments:
            out["scienceInstruments"] = instruments
        if modes:
            out["observingModes"] = modes

        # Remove koAngles_Sun from top level if it exists
        # (it's now in starlightSuppressionSystems)
        if "koAngles_Sun" in out:
            del out["koAngles_Sun"]

        # Apply any additional kwargs as top-level overrides
        if kwargs:
            for key, value in kwargs.items():
                out[key] = value
                logger.info(f"Applied override: {key} = {value}")

        # Reorder output to match typical EXOSIMS structure:
        # 1. Top-level parameters (non-array, non-object, excluding special arrays)
        # 2. erange, arange, Rprange, optional_filters
        # 3. Other objects (anything not in structured_keys or special)
        # 4. scienceInstruments
        # 5. starlightSuppressionSystems
        # 6. observingModes
        # 7. modules
        # 8. completeness_specs (special, goes after modules)

        # Separate parameters into categories
        top_level = {}
        special_arrays = {}
        structured = {}
        other_objects = {}
        completeness_specs = None

        # Special arrays that go before scienceInstruments
        special_array_keys = [
            "err_progression",
            "erange",
            "arange",
            "Rprange",
            "optional_filters",
        ]

        structured_keys = [
            "scienceInstruments",
            "starlightSuppressionSystems",
            "observingModes",
            "modules",
        ]

        for key, value in out.items():
            if key in structured_keys:
                structured[key] = value
            elif key in special_array_keys:
                special_arrays[key] = value
            elif key == "completeness_specs":
                completeness_specs = value
            elif isinstance(value, (dict, list)) and key != "modules":
                other_objects[key] = value
            else:
                top_level[key] = value

        # Reconstruct in desired order
        ordered_out = {}
        ordered_out.update(top_level)
        # Add special arrays before scienceInstruments
        for key in special_array_keys:
            if key in special_arrays:
                ordered_out[key] = special_arrays[key]
        # Add other objects before structured keys
        ordered_out.update(other_objects)
        if "scienceInstruments" in structured:
            ordered_out["scienceInstruments"] = structured["scienceInstruments"]
        if "starlightSuppressionSystems" in structured:
            ordered_out["starlightSuppressionSystems"] = structured[
                "starlightSuppressionSystems"
            ]
        if "observingModes" in structured:
            ordered_out["observingModes"] = structured["observingModes"]
        if "modules" in structured:
            ordered_out["modules"] = structured["modules"]
        # Add completeness_specs after modules
        if completeness_specs is not None:
            ordered_out["completeness_specs"] = completeness_specs

        with open(output_path, "w") as f:
            json.dump(ordered_out, f, indent=4)

        logger.info(f"Exported AYO parameters to EXOSIMS file: {output_path}")
