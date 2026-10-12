from datetime import datetime

def format_duration(start: str, end: str) -> str:
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    if end_dt < start_dt:
        raise ValueError("End date must not be earlier than start date.")
    td = end_dt - start_dt
    total_seconds = int(td.total_seconds())
    days = td.days
    remaining = total_seconds - days * 86400
    hours = remaining // 3600
    minutes = (remaining % 3600) // 60
    parts = []
    if days:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if not parts:
        return "0 minutes"
    return ", ".join(parts)
