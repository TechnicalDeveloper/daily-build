# Days in Month Helper

Build a function `days_in_month` that returns the number of days in a given month and year, accounting for leap years.

**Signature:**
```python
def days_in_month(year: int, month: int) -> int:
    ...
```

**Edge Cases:**
1. Invalid month values (less than 1 or greater than 12) should raise a `ValueError`.
2. Negative year values or year 0 should raise a `ValueError`.
3. February in a leap year vs. a non-leap year must be handled correctly (leap years: divisible by 4 but not by 100 unless also divisible by 400).
