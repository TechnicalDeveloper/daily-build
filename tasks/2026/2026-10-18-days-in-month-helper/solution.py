from calendar import monthrange

def days_in_month(year: int, month: int) -> int:
    if not isinstance(year, int) or not isinstance(month, int):
        raise ValueError("Year and month must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be a positive integer (>= 1)")
    _, days = monthrange(year, month)
    return days
