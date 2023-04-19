"""This module is the entry point of the package.

This is the code which is executed when doing something like: python -m next_weekday.
"""

import argparse
import datetime

from next_weekday.next_weekday import nb_days_until_next_weekday

parser = argparse.ArgumentParser(
    description=(
        "Find the number of days until the next given weekday from a specific date."
    ),
    prog="python -m next_weekday",
)
parser.add_argument(
    "--date",
    type=str,
    help="the reference date to use (the date of today by default).",
    default=None,
)
parser.add_argument(
    "--weekday",
    type=str,
    help="the weekday for which to find the number of days (sunday by default).",
    default="sunday",
)

args = parser.parse_args()

if args.date is not None:
    args.date = datetime.datetime.strptime(args.date, r"%Y-%m-%d")

print(
    f"The number of days until {args.weekday.capitalize()} from {args.date} "
    f"is {nb_days_until_next_weekday(date=args.date, weekday=args.weekday)}."
)
