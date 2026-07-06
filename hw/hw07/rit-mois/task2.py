def area_of_rectangle(a, b):
    """
    Calculates the area of rectangle.

    :param a: width of rectangle
    :param b: length of rectangle
    :return: area of rectangle
    """
    return a * b


def area_of_triangle(a, b):
    """
    Calculates the area of triangle.

    :param a: base of triangle
    :param b: height of triangle
    :return: area of rectangle
    """
    return (a * b) / 2


def area_of_circle(a):
    """
    Calculates the area of circle.

    :param a: radius of circle
    :return: area of circle
    """
    return 3.14 * a ** 2


def calculate_area_of_shape(shape: str):
    """Calculates the area of shape, depending on shape.

    :param shape: shape
    :return: area of shape
    """
    match shape:
        case 'rectangle':
            a = int(input("Enter side a: "))
            b = int(input("Enter side b: "))
            return area_of_rectangle(a, b)
        case 'triangle':
            a = int(input("Enter side a: "))
            b = int(input("Enter side b: "))
            return area_of_triangle(a, b)
        case 'circle':
            a = int(input("Enter radius: "))
            return area_of_circle(a)
        case _:
            return "unsupported"


shape = input("Enter a shape: ")
print(f'Area of {shape} is {calculate_area_of_shape(shape)}')
