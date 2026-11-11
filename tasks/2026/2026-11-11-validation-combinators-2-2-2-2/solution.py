def all_of(*validators):
    'Return a validator that succeeds when every validator succeeds.'
    def validate(value):
        return all(v(value) for v in validators)
    return validate

def any_of(*validators):
    'Return a validator that succeeds when at least one validator succeeds.'
    def validate(value):
        return any(v(value) for v in validators)
    return validate

def none_of(*validators):
    'Return a validator that succeeds when no validator succeeds.'
    def validate(value):
        return not any(v(value) for v in validators)
    return validate

def negate(validator):
    'Return a validator that inverts the result of the given validator.'
    def validate(value):
        return not validator(value)
    return validate
