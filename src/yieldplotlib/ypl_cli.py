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
from docopt import docopt
from yieldplotlib.load.ayo_directory import AYODirectory
from yieldplotlib.load.exosims_directory import EXOSIMSDirectory
from yieldplotlib.pipeline import ypl_pipeline


def main():
    runs = []
    arguments = docopt(__doc__, version='0.1')
    run_paths = arguments["PATH"]

    if is_superdir(run_paths):
        run_dirs = glob.glob(f"{run_paths}/*")
    else:
        run_dirs = list(run_paths)

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


run_paths = ("/Users/ssteiger/repos/yieldplotlib/docs/tutorials/sample_data/exosims")
runs = []
EXOSIMSDirectory(Path(run_paths[0]))
# if is_superdir(run_paths):
#     run_dirs = glob.glob(f"{run_paths}/*")
# else:
#     run_dirs = list(run_paths)
#
# print(run_dirs)
# for run_dir in run_dirs:
#     print(run_dir)
#     if is_ayo(run_dir):
#         runs.append(AYODirectory(Path(run_dir)))
#     else:
#         runs.append(EXOSIMSDirectory(Path(run_dir)))
#
# ypl_pipeline(runs)
