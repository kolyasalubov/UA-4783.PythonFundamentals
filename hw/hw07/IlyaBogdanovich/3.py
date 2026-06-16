def dictionary(string: str) -> dict:
    """
    this function calculates the number of characters included in given string
    input parameters: str
    output: dict
    """
    result = {}
    for value in string:
        result.setdefault(value, string.count(value))
    return result