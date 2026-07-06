import math

def func_rectangle(a, b):
    return a * b

def func_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def func_circle(r):
    return math.pi * r ** 2



while True:
    print("Ця програма допоможе тобі обчислити плоші таких фігур введи номер фігури")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Круг")
    print("4. Вийти")

    while True:
        try:
            choise = int(input("Введіть число (1-4): "))
            if choise >= 1 and choise <= 4:
                break
            else:
                print("Оберіть число від 1 до 4")
        except ValueError:
            print("Будь ласка, введіть правильне число!")

    if choise == 4:
        print("До побачення!")
        break

    if choise == 1:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        print("Площа прямокутника:", func_rectangle(a, b))

    elif choise == 2:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))
        print("Площа трикутника:", func_triangle(a, b, c))

    elif choise == 3:
        r = float(input("Введіть радіус: "))
        print("Площа круга:", func_circle(r))