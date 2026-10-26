def ok():
    def validator(value):
        return (True, value)
    return validator

def fail(error_message):
    def validator(value):
        return (False, error_message)
    return validator

def all_of(*validators):
    def validator(value):
        for v in validators:
            success, result = v(value)
            if not success:
                return (False, result)
        return (True, value)
    return validator

def one_of(*validators):
    def validator(value):
        errors = []
        for v in validators:
            success, result = v(value)
            if success:
                return (True, result)
            else:
                errors.append(result)
        return (False, errors)
    return validator

def transform(validator, func):
    def new_validator(value):
        success, result = validator(value)
        if success:
            try:
                transformed = func(result)
                return (True, transformed)
            except Exception as e:
                return (False, str(e))
        else:
            return (False, result)
    return new_validator

def satisfies(predicate, error_message):
    def validator(value):
        if predicate(value):
            return (True, value)
        else:
            return (False, error_message)
    return validator
