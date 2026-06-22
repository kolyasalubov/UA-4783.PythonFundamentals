def rectangle(x, y: float) -> float:
    """
    this function calculates the area of rectangle using given dimensions
    input parameters: float
    output: float
    """
    return(x * y)


def triangle(a, s: float) -> float:
    """
    this function calculates the area of triangle using given dimensions
    input parameters: float
    output: float
    """
    return(a * s / 2)


def circle(r: float) -> float:
    """
    this function calculates the area of circle using given radius
    input parameters: float
    output: float
    """
    return(3.14 * r * r)


choice = int(input("This program can calculate an area of a rectangle, triangle or circle. \nPlease enter 1 for rectangle, 2 for triangle or 3 for circle \n"))
if choice == 1:
    x = float(input("Please enter the length of your rectangle \n"))
    y = float(input("Please enter the width of your rectangle \n"))
    print("The area of your rectangle is", rectangle(x, y))
elif choice == 2:
    a = float(input("Please enter the length of the base of your triangle \n"))
    s = float(input("Please enter the height of your rectangle \n"))
    print("The area of your triangle is", triangle(a, s))
elif choice == 3:
    r = float(input("Please enter the radius of your circle\n"))
    print("The area of your circle is", circle(r))
else:
    print("Wrong input data")

