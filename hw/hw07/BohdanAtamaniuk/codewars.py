#1 - Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

#2 - Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round((((x2-x1)**2)+((y2-y1)**2))**0.5, 2)
    # Your code here

#3 - No yelling!
def filter_words(st):
    return " ".join(st.split()).capitalize()

#4 - Convert a Number to a String!
def number_to_string(num):
    return str(num)

#5 - Reversing Words in a String
def reverse(st):
    words = st.split()
    st = []
    for word in words[::-1]:
        st.append(word)
    return ' '.join(st)

#better
def reverse(st):
    st = st.split()
    return ' '.join(st[::-1]) 

#6 - Reverse List Order
def reverse_list(l):
    return l[::-1]

#7 - ultiples of 3 or 5
def solution(number):
    numbers = []
    a = 1
    result = 0
    if number > 0:
        while a < number:
            numbers.append(a)
            a += 1
        for n in numbers:
            if n % 3 == 0 or n % 5 == 0:
                result = result + n
            else:
                continue
        return result
    else:
        return 0

#8 - Will u make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump<=fuel_left*mpg:
        return True
    else:
        return False

#9 - Are You Playing Banjo?
def are_you_playing_banjo(name):
    name_check = name.lower()
    if name_check[0:1] == "r":
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#10 - Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
#11 - Counting sheep...
def count_sheeps(sheep):
    numbers = 0
    for b in sheep:
        if b == True:
            numbers +=1
        else:
            continue
    return numbers

#12 - Is this my tail?
def correct_tail(body, tail):
    sub = body[-1:]
    if sub == tail:
        return True
    else:
        return False
