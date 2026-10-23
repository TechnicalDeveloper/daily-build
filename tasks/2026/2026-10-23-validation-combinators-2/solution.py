def is_integer():
    def validator(value):
        if not isinstance(value, int):
            return "Value is not an integer"
        return None
    return validator


def is_positive():
    def validator(value):
        if not isinstance(value, int) or value <= 0:
            return "Value is not positive"
        return None
    return validator


def is_non_empty_string():
    def validator(value):
        if not isinstance(value, str) or len(value) == 0:
            return "Value is not a non-empty string"
        return None
    return validator


def is_email():
    import re
    pattern = r'^[^@]+@[^@]+\.[^@]+$'
    def validator(value):
        if not isinstance(value, str) or not re.match(pattern, value):
            return "Value is not a valid email"
        return None
    return validator


def and_(v1, v2):
    def validator(value):
        err1 = v1(value)
        if err1 is not None:
            return err1
        return v2(value)
    return validator


def or_(v1, v2):
    def validator(value):
        err1 = v1(value)
        if err1 is None:
            return None
        return v2(value)
    return validator


def not_(v):
    def validator(value):
        err = v(value)
        if err is None:
            return "Validation should have failed"
        return None
    return validator


def all_(*validators):
    def validator(value):
        for v in validators:
            err = v(value)
            if err is not None:
                return err
        return None
    return validator


def any_(*validators):
    def validator(value):
        last_err = "No validators provided"
        for v in validators:
            err = v(value)
            if err is None:
                return None
            last_err = err
        return last_err
    return validator


def maybe(v):
    def validator(value):
        if value is None:
            return None
        return v(value)
    return validator
