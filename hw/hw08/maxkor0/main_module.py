import area
shape = input("Enter your shape(rectangle, triangle, or circle): ").casefold()
if shape == "rectangle":
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print(area.s_rectangle(l, b))
elif shape == "triangle":
    h = float(input("Enter height: "))
    b = float(input("Enter base: "))
    print(area.s_triangle(h, b))
elif shape == "circle":
    r = float(input("Enter radius: "))
    print(area.s_circle(r))
else:
    print("Invalid shape")
