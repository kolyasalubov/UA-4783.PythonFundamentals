from math import pi, pow
import task3_part_1 as tp1

while True:
    figure = input("\nEnter the figure: circle, triangle, rectangle.\nType 'stop' if you want to stop: ")
    if figure == "stop":
        break
    elif figure == "triangle":
        h = float(input("Enter h: "))
        a = float(input("Enter a: "))
        print("\nArea of triangle: ", tp1.triangle_area(h, a ))
    elif figure == "rectangle":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("\nArea of rectangle: ", tp1.rectangle_area(a,b))
    elif figure == "circle":
        r = float(input("Enter r: "))
        print("\nArea of circle: ", tp1.circle_area(r, pi,pow))
    else:
        print("\nInvalid figure, please enter a valid figure")