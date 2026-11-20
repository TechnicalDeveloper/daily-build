import re

def is_string(value):
    if not isinstance(value, str):
        raise ValueError('must be a string')
    return value

def is_integer(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError('must be an integer')
    return value

def min_length(n):
    def validator(value):
        try:
            length = len(value)
        except TypeError:
            raise ValueError('must have a length')
        if length < n:
            raise ValueError(f'must have length >= {n}')
        return value
    return validator

def regex(pattern):
    rx = re.compile(pattern)
    def validator(value):
        if not isinstance(value, str):
            raise ValueError('must be a string')
        if rx.fullmatch(value) is None:
            raise ValueError(f'must match pattern {pattern!r}')
        return value
    return validator

def all_of(*validators):
    def validator(value):
        for v in validators:
            v(value)
        return value
    return validator

def any_of(*validators):
    def validator(value):
        errors = []
        for v in validators:
            try:
                v(value)
                return value
            except ValueError as e:
                errors.append(str(e))
        raise ValueError('; '.join(errors) if errors else 'no validator accepted')
    return validator

def optional(validator):
    def validate(value):
        if value is not None:
            validator(value)
        return value
    return validate
