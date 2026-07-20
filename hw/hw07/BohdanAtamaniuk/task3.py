

def count_chars(text) -> dict:
    '''
    This funcion for calculate number of characters included on given string

    Parameters:
    text(str): The string for calculate 

    return: chars(dict)
    '''
    chars = {}
    for char in text:
        if char in chars.keys():
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1
    return chars
    
print(count_chars(input("Print any word: ")))