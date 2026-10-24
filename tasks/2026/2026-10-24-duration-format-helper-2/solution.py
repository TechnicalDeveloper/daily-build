def format_duration(seconds):
    if seconds < 0:
        raise ValueError('Negative duration')
    if seconds == 0:
        return '0 seconds'
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days > 0:
        parts.append(f'{days} day' + ('s' if days != 1 else ''))
    if hours > 0:
        parts.append(f'{hours} hour' + ('s' if hours != 1 else ''))
    if minutes > 0:
        parts.append(f'{minutes} minute' + ('s' if minutes != 1 else ''))
    if seconds > 0:
        parts.append(f'{seconds} second' + ('s' if seconds != 1 else ''))
    if len(parts) == 1:
        return parts[0]
    return ', '.join(parts[:-1]) + ' and ' + parts[-1]
