def calculate_characters(string: str):
    """This function calculates the characters given a string"""
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1

    return result

print(calculate_characters("hello"))
