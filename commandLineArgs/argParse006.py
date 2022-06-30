"""
Combination of Positional adn optional Args

$ python3 prog.py
usage: prog.py [-h] [-v] square
prog.py: error: the following arguments are required: square

$ python3 prog.py 4
16

$ python3 prog.py 4 --verbose
the square of 4 equals 16

$ python3 prog.py --verbose 4
the square of 4 equals 16
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)
