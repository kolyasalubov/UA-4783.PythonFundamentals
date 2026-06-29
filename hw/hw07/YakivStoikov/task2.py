import math
def get_rectangle_area(length: float, width: float) -> float:
    """
    Returns the area of a rectangle.

    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Area of the rectangle
    """
    return length * width

def get_triangle_area(base: float, height: float) -> float:
    """
    Returns the area of a triangle.

    :param base: Base of the triangle
    :param height: Height of the triangle
    :return: Area of the triangle
    """
    return 0.5 * base * height

def get_circle_area(radius: float) -> float:
    """
    Returns the area of a circle.

    :param radius: Radius of the circle
    :return: Area of the circle
    """
    return math.pi * radius ** 2

while True:
    shape = input("Enter the shape (rectangle, triangle, circle): ").strip().lower()
    if shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = get_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
        break
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = get_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
        break
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = get_circle_area(radius)
        print(f"The area of the circle is: {area}")
        break
    else:
        print("Invalid shape entered. Please enter rectangle, triangle, or circle.")
