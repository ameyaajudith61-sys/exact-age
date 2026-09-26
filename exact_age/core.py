"""Calculate a person's exact age from their date of birth."""

import calendar
from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Age:
    years: int
    months: int
    days: int
    total_days: int

    def __str__(self) -> str:
        return f"{self.years} years, {self.months} months, {self.days} days"


def _parse_date(value) -> date:
    """Accept a date object or a YYYY-MM-DD string."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError as exc:
            raise ValueError(
                f"Invalid date string '{value}'. Expected format: YYYY-MM-DD"
            ) from exc
    raise TypeError(
        f"Unsupported type {type(value)} for date. "
        "Use a date object or YYYY-MM-DD string."
    )


def _birthday_in_year(dob: date, year: int) -> date:
    """Use March 1 for a February 29 birthday in non-leap years."""
    try:
        return dob.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def calculate_age(date_of_birth, reference_date=None) -> Age:
    """Calculate age in years, months, and days as of the reference date."""
    dob = _parse_date(date_of_birth)
    ref = (
        _parse_date(reference_date)
        if reference_date is not None
        else date.today()
    )

    if dob > ref:
        raise ValueError("Date of birth cannot be in the future.")

    total_months = (ref.year - dob.year) * 12 + ref.month - dob.month

    def anniversary(months_after: int) -> date:
        month_index = dob.year * 12 + dob.month - 1 + months_after
        year, zero_based_month = divmod(month_index, 12)
        month = zero_based_month + 1
        day = min(dob.day, calendar.monthrange(year, month)[1])
        return date(year, month, day)

    while total_months > 0 and anniversary(total_months) > ref:
        total_months -= 1

    years, months = divmod(total_months, 12)
    days = (ref - anniversary(total_months)).days

    return Age(years, months, days, (ref - dob).days)


def is_birthday_today(date_of_birth, reference_date=None) -> bool:
    """Check whether the birthday falls on the reference date."""
    dob = _parse_date(date_of_birth)
    ref = (
        _parse_date(reference_date)
        if reference_date is not None
        else date.today()
    )
    return _birthday_in_year(dob, ref.year) == ref


def next_birthday(date_of_birth, reference_date=None) -> date:
    """Return the next birthday, or today's birthday if it falls today."""
    dob = _parse_date(date_of_birth)
    ref = (
        _parse_date(reference_date)
        if reference_date is not None
        else date.today()
    )

    birthday = _birthday_in_year(dob, ref.year)
    if birthday < ref:
        birthday = _birthday_in_year(dob, ref.year + 1)
    return birthday

