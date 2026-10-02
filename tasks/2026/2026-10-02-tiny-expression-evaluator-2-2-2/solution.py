def evaluate(expr: str) -> int:
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isdigit():
            j = i
            while j < n and expr[j].isdigit():
                j += 1
            tokens.append(int(expr[i:j]))
            i = j
            continue
        if expr[i] in '+-*/':
            tokens.append(expr[i])
            i += 1
            continue
        raise ValueError(f"Invalid character: {expr[i]}")

    # Process * and /
    i = 1
    while i < len(tokens) - 1:
        if isinstance(tokens[i], str) and tokens[i] in '*/':
            left = tokens[i-1]
            right = tokens[i+1]
            if tokens[i] == '*':
                result = left * right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                result = left // right
            tokens = tokens[:i-1] + [result] + tokens[i+2:]
            i = 1
        else:
            i += 1

    # Process + and -
    i = 1
    while i < len(tokens) - 1:
        if isinstance(tokens[i], str) and tokens[i] in '+-':
            left = tokens[i-1]
            right = tokens[i+1]
            if tokens[i] == '+':
                result = left + right
            else:
                result = left - right
            tokens = tokens[:i-1] + [result] + tokens[i+2:]
            i = 1
        else:
            i += 1

    if len(tokens) != 1:
        raise ValueError("Invalid expression")
    return tokens[0]
