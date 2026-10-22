from typing import Any, Callable, Tuple, Optional

# Type alias for a validator
Validator = Callable[[Any], Tuple[bool, Optional[str]]]

def predicate(check: Callable[[Any], bool], error_msg: str) -> Validator:
    """Create a validator from a predicate function."""
    def validator(value: Any) -> Tuple[bool, Optional[str]]:
        if check(value):
            return (True, None)
        else:
            return (False, error_msg)
    return validator

def all_of(*validators: Validator) -> Validator:
    """Combine validators with logical AND."""
    def validator(value: Any) -> Tuple[bool, Optional[str]]:
        for v in validators:
            success, err = v(value)
            if not success:
                return (False, err)
        return (True, None)
    return validator

def any_of(*validators: Validator) -> Validator:
    """Combine validators with logical OR."""
    def validator(value: Any) -> Tuple[bool, Optional[str]]:
        errors = []
        for v in validators:
            success, err = v(value)
            if success:
                return (True, None)
            else:
                errors.append(err)
        error_msg = '; '.join(errors) if errors else 'No validators provided'
        return (False, error_msg)
    return validator

def optional(validator: Validator) -> Validator:
    """Allow None values to pass without validation."""
    def validator_func(value: Any) -> Tuple[bool, Optional[str]]:
        if value is None:
            return (True, None)
        else:
            return validator(value)
    return validator_func

def not_validator(validator: Validator) -> Validator:
    """Negate the result of a validator."""
    def validator_func(value: Any) -> Tuple[bool, Optional[str]]:
        success, err = validator(value)
        if success:
            return (False, 'Value not expected')
        else:
            return (True, None)
    return validator_func
