'''
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

yieldplotlib command line interface.

Usage:
  run_ypl PATH

Options:
  -h, --help  Show this help message and exit.
'''

import os
import glob
from pathlib import Path

import numpy as np
from docopt import docopt
from yieldplotlib.load.ayo_directory import AYODirectory
from yieldplotlib.load.exosims_directory import EXOSIMSDirectory
from yieldplotlib.pipeline import ypl_pipeline


def main():
    runs = []
    arguments = docopt(__doc__, version='0.1')
    run_paths = arguments["PATH"]

    if is_superdir(run_paths):
        run_dirs = [r.path for r in os.scandir(run_paths) if r.is_dir()]
    else:
        run_dirs = [run_paths]

    for run_dir in run_dirs:
        print(run_dir)
        if is_ayo(run_dir):
            runs.append(AYODirectory(Path(run_dir)))
        else:
            runs.append(EXOSIMSDirectory(Path(run_dir)))

    ypl_pipeline(runs)


def is_superdir(path):
    for directory in glob.glob(f"{path}/*"):
        if not os.path.isdir(directory):
            return False
    return True


def is_ayo(path):
    for file in os.listdir(path):
        if file.endswith(".ayo"):
            return True
    return False

