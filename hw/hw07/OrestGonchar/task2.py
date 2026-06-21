import math
def rectangle_square(a,b):
    return a*b
def triangle_square(a, b):
    return 0.5 * a * b
def circle_square(r):
    return math.pi*r**2
choice = input('You have to choose 1 (rectangle_square), 2 (triangle_square) or 3( circle_square): ')
if choice == '1':
    a = int(input('Enter side length'))
    b = int(input('Enter width of the square'))
    print(rectangle_square(a,b))
elif choice == '2':
    a = int(input('Enter side'))
    b = int(input('Enter height drawn to the side'))
    print(triangle_square(a,b))
elif choice == '3':
    r = int(input('Enter radius'))
    print(circle_square(r))