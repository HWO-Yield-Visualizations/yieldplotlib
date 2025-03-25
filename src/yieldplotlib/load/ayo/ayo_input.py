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
            + pp.Suppress(";")
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
