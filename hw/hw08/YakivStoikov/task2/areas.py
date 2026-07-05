from math import pi, pow

def rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle."""
    return length * width

def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle."""
    return pi * pow(radius, 2)

def triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle."""
    return 0.5 * base * height
