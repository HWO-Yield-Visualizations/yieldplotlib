"""TODO."""

from yieldplotlib.logger import logger

# Set initial logger level
logger.setLevel("DEBUG")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

# Change the logger level to WARNING
logger.setLevel("WARNING")
logger.info("This info message will not appear")
logger.warning("This is a warning message after level change")

# Simple test with potential error
x = 0
try:
    result = 10 / x
    logger.info(f"Result of division is {result}")
except ZeroDivisionError as e:
    logger.error(f"An error occurred: {e}")
