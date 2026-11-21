def format_duration(seconds):
    if seconds == 0:
        return "now"
    seconds = abs(seconds)
    units = [
        ("year", 365*24*60*60),
        ("day", 24*60*60),
        ("hour", 60*60),
        ("minute", 60),
        ("second", 1)
    ]
    parts = []
    for name, unit_sec in units:
        if seconds >= unit_sec:
            value = seconds // unit_sec
            seconds %= unit_sec
            if value == 1:
                parts.append(f"{value} {name}")
            else:
                parts.append(f"{value} {name}s")
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " and " + parts[-1]
