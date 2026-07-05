def rectangular_area(a,b):
    '''The function returns the area of a rectangle.'''
    return a * b

def circle_area(r):
    '''The function returns the area of a circle.'''
    return 3.14 * r**2

def triangle_area(a,h):
    '''The function returns the area of a triangle.'''
    return 0.5 * a * h

def area_calculation(shape, *args):
    if shape == "rectangle":
        return rectangular_area(*args)
    elif shape == "circle":
        return circle_area(*args)
    elif shape == "triangle":
        return triangle_area(*args)
    else:
        return "Invalid shape"

print(area_calculation("rectangle", 10, 20))
print(area_calculation("circle", 10))
print(area_calculation("triangle", 10, 20))