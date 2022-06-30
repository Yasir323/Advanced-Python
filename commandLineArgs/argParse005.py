"""
Optioonal Arguments

$ python3 prog.py -v
verbosity turned on

$ python3 prog.py --help
usage: prog.py [-h] [-v]

options:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-v',
    '--verbosity',
    help="Increase output verbosity",
    action='store_true'
)  # No need to provide a value for verbosity

args = parser.parse_args()
if args.verbosity:
    print("Verbosity on.")
