"""This module tests the functionalities of the core of the package."""

import datetime

import pytest

from next_weekday.next_weekday import nb_days_until_next_weekday


@pytest.mark.parametrize(
    "date, weekday, expected",
    [
        (datetime.datetime(2023, 4, 18), "sunday", 5),
        (datetime.datetime(2023, 4, 19), "sunday", 4),
        (datetime.datetime(2023, 4, 23), "sunday", 7),
        (datetime.datetime(2023, 4, 23), "sunday", 7),
        (datetime.datetime(2023, 5, 30), "sunday", 5),
        (datetime.datetime(2023, 4, 18), "thursday", 2),
        (datetime.datetime(2023, 4, 19), "thursday", 1),
        (datetime.datetime(2023, 4, 21), "thursday", 6),
        (datetime.datetime(2023, 5, 30), "Monday", 6),
        (datetime.datetime(2023, 5, 31), "MONDAY", 5),
    ],
)
def test_nb_days_until_next_weekday(
    date: datetime.datetime, weekday: str, expected: int
) -> None:
    """Tests that we correctly compute the number of days."""
    assert nb_days_until_next_weekday(date=date, weekday=weekday) == expected
