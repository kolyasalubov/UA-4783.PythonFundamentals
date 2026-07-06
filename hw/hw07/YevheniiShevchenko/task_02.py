def rectangle_area(length, width):
    """The function return the area of a rectangle"""
    return length * width

def circle_area(radius):
    """The function return the area of a circle"""
    return 3.14 * radius ** 2

def triangle_area(base, height):
    """The function return the area of a triangle"""
    return 0.5 * base * height

def shape_area(shape, *args):
    """The function return the area of a shape"""
    if shape == "rectangle":
        return rectangle_area(args[0], args[1])
    elif shape == "circle":
        return circle_area(args[0])
    elif shape == "triangle":
        return triangle_area(args[0], args[1])

print(shape_area("circle", 10, 20))