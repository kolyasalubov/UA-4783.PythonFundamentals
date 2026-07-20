def area_rectangle(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

def area_triangle(base, height):
    '''
    Calculate the area of a triangle
    
    Parameters:
    base (float): The base of the triangle
    height (float): The height of the triangle

    return: float ( area of triangle) 
    '''

    return 0.5*base*height

def area_circle(radius):
    '''
    Calculate the ara of circle

    Parameters:
    radius (float): The radius of circle
    PI (float): PI number

    return: float (area of circle)
    '''
    PI = 3.14
    return (radius**2)*PI

area = input("Choose area what u want to calculate(rectangle, triangle, circle): ")

if area == "Circle" or area=="circle":
    radius = float(input("Print radius of the circle (FLOAT): "))
    print("Area is ", area_circle(radius))
elif area == 'Triangle' or area=='triangle':
    base = float(input("Print base of the triangle (FLOAT): "))
    height = float(input("Print height of the triangle (FLOAT): "))
    print("Area is ", area_triangle(base, height))
elif area == "rectangle" or area=='Rectangle':
    length = float(input("Print length of the rectangle (FLOAT): "))
    width = float(input("Print width of the rectangle (FLOAT): "))
    print("Area is ", area_rectangle(length, width))
else:
    print("WE DONT HAVE THIS OPTION!!!")