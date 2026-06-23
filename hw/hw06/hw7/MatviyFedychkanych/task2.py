import math

def area_rectangle(a, b):
    return f"Площа прямокутника: {a * b}"

def area_triangle(a, b, c):
    p = (a + b + c) / 2
    return f"Площа трикутника: {(p * (p - a) * (p - b) * (p - c)) ** 0.5:.4f}"

def area_circle(r):
    return f"Площа кола: {(r**2 * math.pi):.4f}"

choice = input("Оберіть фігуру та напишіть її: rectangle, triangle or circle: ")
if choice == "rectangle":
    a = float(input("Вкажіть довжину прямокутника: "))
    b = float(input("Вкажіть ширину прямокутника: "))
    print(area_rectangle(a, b))
elif choice == "triangle":
    a = float(input("Вкажіть першу сторону: "))
    b = float(input("Вкажіть другу сторону: "))
    c = float(input("Вкажіть третю сторону: "))
    print(area_triangle(a, b, c))
elif choice == "circle":
    r = float(input("Вкажіть радіус кола: "))
    print(area_circle(r))
else:
    print("Невідома фігура, або не повна назва")