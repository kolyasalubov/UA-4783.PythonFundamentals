def triangle_area():
    '''The function calculates the area of a triangle'''
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return base * height / 2
    except ValueError:
        print("Invalid input, please enter a number")


def rectangle_area():
    '''The function calculates the area of a rectangle'''
    try:
        a = float(input("Enter a: "))
        b = float(input("enter b: "))
        return a * b
    except ValueError:
        print("Invalid input, please enter a number")


def circle_area():
    '''The function calculates the area of a circle'''
    try:
        r = float(input("Enter radius: "))
        return 3.14159 * r * r
    except ValueError:
        print("Invalid input, please enter a number")


#Program
while True:
    figure = input("\nEnter the figure: circle, triangle, rectangle.\nType 'stop' if you want to stop: ")
    if figure == "stop":
        break
    elif figure == "triangle":
        print("\nArea of triangle: ", triangle_area())
    elif figure == "rectangle":
        print("\nArea of rectangle: ", rectangle_area())
    elif figure == "circle":
        print("\nArea of circle: ", circle_area())
    else:
        print("\nInvalid figure, please enter a valid figure")
