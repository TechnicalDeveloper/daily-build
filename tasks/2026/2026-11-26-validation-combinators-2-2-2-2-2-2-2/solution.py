def all_of(*validators):
    def validator(value):
        return all(v(value) for v in validators)
    return validator

def any_of(*validators):
    def validator(value):
        return any(v(value) for v in validators)
    return validator

def none_of(*validators):
    def validator(value):
        return not any(v(value) for v in validators)
    return validator

def not_validator(validator):
    def new_validator(value):
        return not validator(value)
    return new_validator
