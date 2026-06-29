def get_character_numbers(some_string: str):
    """
    Prints the count of each character in the given string.
    param some_string: The input string to analyze
    return: None
    """
    char_count = {}
    for char in some_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print (f"The character counts in the string are: {char_count}")

