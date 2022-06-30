"""
Optioonal Arguments


$ python3 prog.py --verbosity 1
verbosity turned on

$ python3 prog.py

$ python3 prog.py --help
usage: prog.py [-h] [--verbosity VERBOSITY]

options:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity

$ python3 prog.py --verbosity
usage: prog.py [-h] [--verbosity VERBOSITY]
prog.py: error: argument --verbosity: expected one argument
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-v',
    '--verbosity',
    help="Increase output verbosity"
)  # Need to provide a value for verbosity

args = parser.parse_args()
if args.verbosity:
    print("Verbosity on.")
