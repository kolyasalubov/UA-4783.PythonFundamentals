### 1.Jenny's secret message ###


# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)
    

# print(greet("Johnny"))


### 2.Simple: Find The Distance Between Two Points ###


# def distance(x1, y1, x2, y2):
#      return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5,2)

     
### 3.No yelling! ###


# def filter_words(st):
#     return ' '.join(st.capitalize().split())

# print(filter_words("Hello,    World!"))


### 4.Convert a Number to a String! ###


# def number_to_string(num):
#     return str(num)

# print(number_to_string(-100))


### 5.Reversing Words in a String ###


# def reverse(st):
#     return ' '.join(st.split()[::-1])

# print(reverse("Hello world"))


### 6.Reverse List Order ###


# def reverse_list(l):
#     return l[::-1]


### 7.Multiples of 3 or 5 ###


# def solution(number):
#     sum = 0
#     if number < 1:
#         return 0
#     else:
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 sum += i
#         return sum


### 8.Will you make it? ###


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if fuel_left * mpg >= distance_to_pump:
#         return True
#     else:
#         return False


### 9.Are You Playing Banjo? ###


# def are_you_playing_banjo(name):
#     if name[0].lower() == "r":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"



### 10.Convert boolean values to strings 'Yes' or 'No’ ###


# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"


### 11.Counting sheep... ###


# def count_sheeps(sheep):
#     sum = 0
#     for i in sheep:
#         if i == True:
#             sum += 1
#     return sum


### 12.Is this my tail? ###


def correct_tail(body, tail):
    return body.endswith(tail)