from areas import rectangle_area, circle_area, triangle_area

from math import pi, pow

shape = input("Enter the shape (rectangle, circle, triangle): ")

if shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print(f"Area: {rectangle_area(length, width)}")
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    print(f"Area: {circle_area(radius)}")
elif shape == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print(f"Area: {triangle_area(base, height)}")
else:
    print("Invalid shape")
    