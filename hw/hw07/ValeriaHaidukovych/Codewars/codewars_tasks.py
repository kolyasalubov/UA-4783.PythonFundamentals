#task1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    

#task2

from math import sqrt
def distance(x1, y1, x2, y2):
    result = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(result, 2)


#task3

def filter_words(st):
    result = " ".join(st.split())
    return result.capitalize()


#task4

def number_to_string(num):
    return str(num)


#task5

def reverse(st):
    return " ".join(st.split()[::-1])


#task6

def reverse_list(l):
    return l[::-1]


#task7

def solution(number):
    result = 0
    if number < 0:
        result = 0
    else:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                result += i
    return result


#task8

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump == mpg * fuel_left


#task9

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    

#task10

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    

#task11

def count_sheeps(sheep):
    return sheep.count(True)


#task12

def correct_tail(body, tail):
    return body[-1] == tail[0]
