def process_request(value):
    """
    Core business logic:
    Takes a number and applies company rules to it.
    """
    if value < 0:
        return None

    # Business rule: multiply by 2 and add 10
    result = (value * 2) + 10
    return result
