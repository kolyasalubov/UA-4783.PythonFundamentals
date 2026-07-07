from math import pi, pow

def rectangle(x, y: float) -> float:
    """
    this function calculates the area of rectangle using given dimensions
    input parameters: float
    output: float
    """
    return round(x * y, 2)


def triangle(a, s: float) -> float:
    """
    this function calculates the area of triangle using given dimensions
    input parameters: float
    output: float
    """
    return round(a * s / 2, 2)


def circle(r: float) -> float:
    """
    this function calculates the area of circle using given radius
    input parameters: float
    output: float
    """
    return round(pi * pow(r, 2), 2)

