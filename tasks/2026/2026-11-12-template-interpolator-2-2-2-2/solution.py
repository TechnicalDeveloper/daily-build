import re

def interpolate(template: str, variables: dict) -> str:
    def repl(match):
        key = match.group(1)
        if key not in variables:
            raise KeyError(key)
        return str(variables[key])
    return re.sub(r'\{([^{}]+)\}', repl, template)
