# exact-age

Calculate a person's exact age in years, months, and days from their date of birth.

## Install

```bash
pip install -e .
```

(Once published to PyPI, this becomes `pip install exact-age`.)

## Usage

```python
from exact_age import calculate_age, is_birthday_today, next_birthday

age = calculate_age("2000-06-15",reference_date="2024-09-26")
print(age)              #  "24 years, 3 months, 11 days"
print(age.years)        # 24
print(age.months)       # 3
print(age.days)         # 11
print(age.total_days)   # total days lived

# Check if today is someone's birthday
print(is_birthday_today("2000-06-15"))

# Find the date of their next birthday
print(next_birthday("2000-06-15"))
```

You can also pass a `reference_date` to calculate age as of any date, and
`date_of_birth`/`reference_date` can be either `"YYYY-MM-DD"` strings or
Python `date` objects.

## Running tests

```bash
pip install pytest
pytest
```

## License

MIT
