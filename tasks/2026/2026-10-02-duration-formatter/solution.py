def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"
    
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    components = []
    if days > 0:
        components.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        components.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        components.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        components.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return ", ".join(components)
