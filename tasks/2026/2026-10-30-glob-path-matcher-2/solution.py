import re


def match_path(pattern: str, path: str) -> bool:
    """Return True if path matches the glob pattern."""
    regex_parts = []
    i = 0
    n = len(pattern)
    while i < n:
        c = pattern[i]
        if c == '*':
            if i + 1 < n and pattern[i + 1] == '*':
                # Check that ** is a whole segment
                start_ok = (i == 0) or (pattern[i - 1] == '/')
                end_ok = (i + 2 == n) or (pattern[i + 2] == '/')
                if not (start_ok and end_ok):
                    raise ValueError("** must be a whole path segment")
                if i + 2 < n and pattern[i + 2] == '/':
                    # Consume the following slash so that '**/' can match zero or more segments
                    regex_parts.append('(?:[^/]+/)*')
                    i += 3
                else:
                    regex_parts.append('.*')
                    i += 2
            else:
                regex_parts.append('[^/]*')
                i += 1
        elif c == '?':
            regex_parts.append('[^/]')
            i += 1
        else:
            regex_parts.append(re.escape(c))
            i += 1
    regex = '^' + ''.join(regex_parts) + '$'
    return re.fullmatch(regex, path) is not None
