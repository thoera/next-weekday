"""This module defines the core of the package."""

import datetime
from typing import Optional

WEEKDAYS = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


def nb_days_until_next_weekday(
    date: Optional[datetime.datetime], weekday: str = "sunday"
) -> int:
    """Returns the number of days between a date and the next given weekday."""
    if weekday.casefold() not in WEEKDAYS:
        raise ValueError(f"`weekday` should be one of {', '.join(WEEKDAYS)}.")

    if date is None:
        date = datetime.datetime.now()

    nb_days = WEEKDAYS[weekday.casefold()] - date.weekday()

    # If the current day is already the weekday to found, the next one is in... 7 days!
    if nb_days == 0:
        nb_days = 7

    # If the current day is next week, subtract the number of days computed
    # from a whole week.
    if nb_days < 0:
        nb_days = 7 + nb_days

    return nb_days
