def all_of(*validators):
    """Return a validator that passes if all given validators pass."""
    def validator(value):
        return all(v(value) for v in validators)
    return validator


def any_of(*validators):
    """Return a validator that passes if at least one given validator passes."""
    def validator(value):
        return any(v(value) for v in validators)
    return validator


def none_of(*validators):
    """Return a validator that passes if none of the given validators pass."""
    def validator(value):
        return not any(v(value) for v in validators)
    return validator


def not_validator(validator):
    """Return a validator that negates the given validator."""
    def inner(value):
        return not validator(value)
    return inner
