"""yieldplotlib command line interface.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@
@@@  @@@@@@@ @@@  @@   @@@@@@@@@  @@@@@@@
@@@@  @@@@@  @@@   @@@@  @@@@@@@  @@@@@@@
@@@@@ @@@@  @@@@  @@@@@@  @@@@@@  @@@@@@@
@@@@@@ @@  @@@@@  @@@@@@  @@@@@@  @@@@@@@
@@@@@@  @ @@@@@@  @@@@@  @@@@@@@  @@@@@@@
@@@@@@@   @@@@@@  @     @@@@@@@@@     @@@
@@@@@@@  @@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@
@@@@    @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Usage:
  run_ypl PATH

Options:
  -h, --help  Show this help message and exit.
"""

import glob
import os
from pathlib import Path

from docopt import docopt

from yieldplotlib.load.ayo_directory import AYODirectory
from yieldplotlib.load.exosims_directory import EXOSIMSDirectory
from yieldplotlib.pipeline import ypl_pipeline


def main():
    """Runs the command line interface."""
    runs = []
    arguments = docopt(__doc__, version="0.1")
    run_paths = arguments["PATH"]

    if is_superdir(run_paths):
        run_dirs = glob.glob(f"{run_paths}/*")
    else:
        run_dirs = [run_paths]

    for run_dir in run_dirs:
        if is_ayo(run_dir):
            runs.append(AYODirectory(Path(run_dir)))
        else:
            runs.append(EXOSIMSDirectory(Path(run_dir)))

    ypl_pipeline(runs)


def is_superdir(path):
    """True if a directory only contains other directories."""
    for directory in glob.glob(f"{path}/*"):
        if not os.path.isdir(directory):
            return False
    return True


def is_ayo(path):
    """True if a directory is an AYO run directory."""
    for file in os.listdir(path):
        if file.endswith(".ayo"):
            return True
    return False
