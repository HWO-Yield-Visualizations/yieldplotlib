"""Node for handling input .ayo files."""

from pathlib import Path

import astropy.units as u
import numpy as np
import pyparsing as pp
from lod_unit import lod

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

    def _get(self, key: str):
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

        # Define key-value pair with type, optional unit, and optional comments
        key_value = (
            identifier.setResultsName("key")
            + pp.Suppress("=")
            + (number | string | array).setResultsName("value")
            + pp.Suppress(";")
            + pp.Optional(unit_literal)
            + pp.Optional(pp.SkipTo("{").setResultsName("comment_before_type"))
            + type_literal
            + pp.Optional(pp.SkipTo(pp.lineEnd()).setResultsName("comment_after_type"))
        )

        # Split the raw data into individual lines
        input_file_lines = self.raw_data.split("\n")

        for line_number, line in enumerate(input_file_lines, start=1):
            line = line.strip()

            # Skip empty lines and lines starting with ';' or '#'
            if not line or line.startswith(";") or line.startswith("#"):
                continue

            # Parse the line using the defined parser
            parsed = key_value.parseString(line, parseAll=True)

            # Extract key, value, and type from the parsed result
            key = parsed["key"]
            type_ = parsed["type"].lower()
            value = parsed["value"][0]
            if "units" in parsed:
                unit = parsed["units"]
                value *= unit

            # Depending on the type, process the value accordingly
            if type_ == "scalar":
                # Value is already converted to int or float
                self.data[key] = value
                logger.debug(f"Parsed scalar: {key} = {value}")

            elif type_ == "string":
                # Value is already a string without quotes
                self.data[key] = value
                logger.debug(f"Parsed string: {key} = {value}")

            elif type_ == "array":
                # Value is a list of scalars or strings
                self.data[key] = value
                logger.debug(f"Parsed array: {key} = {value}")
            else:
                # Unsupported type; treat value as string and log a warning
                self.data[key] = value
                logger.warning(
                    (
                        f"Unknown type '{type_}' for key '{key}' at line {line_number}."
                        " Treated as string."
                    )
                )

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
