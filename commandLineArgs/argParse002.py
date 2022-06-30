"""
Positional Arguments
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', help="Echo the string you use here.")
args = parser.parse_args()
print(args.echo)
