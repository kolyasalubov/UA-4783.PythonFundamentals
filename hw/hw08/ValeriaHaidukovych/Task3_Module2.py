import Task3_Module1
import math

choice_func = input("Enter shape type: ")
if choice_func == "rectangle":
    Task3_Module1.area_rectangle(float(input("Input a: ")), float(input("Input b: ")))
elif choice_func == "triangle":
    Task3_Module1.area_triangle(float(input("Input a: ")), float(input("Input h: ")))
elif choice_func == "circle":
    Task3_Module1.area_circle(float(input("Input r: ")), math.pi, math.pow)
                