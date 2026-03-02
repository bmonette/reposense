# This file handles the command line interface (CLI)
#
# What it does:
#
# - Parses commands (scan, options, flags).
# - Validates input paths.
# - Calls the scanner.
# - Triggers report generation.
# - Displays results.

import argparse
from pathlib import Path


def build_parser():
    '''
    Builds the command line argument parser.
    '''

    # Creates the ArgumentParser object.
    parser = argparse.ArgumentParser(description='RepoSense is a local project repository analyzer that generates analysis reports')

    parser.add_argument("scan", type=Path, help="Path to the repository to scan")
    parser.add_argument("--ignore", type=Path, nargs="+", metavar="PATTERN", help="Ignore the specified extensions")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--max-size", type=int, help="Flag large files larger than this size in bytes")

    return parser


if __name__ == "__main__":
    raise SystemExit(build_parser())
