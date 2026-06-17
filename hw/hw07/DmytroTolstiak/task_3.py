def number_of_characters_in_a_string():
    string_ = input("\nEnter the string you want to count: ")
    count = {}
    for char in string_:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
for key, value in number_of_characters_in_a_string().items():
    print(f"{key} : {value}")
