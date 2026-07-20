import area
calculate = input('Enter what area do u want calculate: (r(rectangle), c(circle), t(triangle)\n')
if calculate.lower() == 'c':
    radius = float(input('Enter a radius of the circle: \n'))
    print(area.circle_area(radius))
elif calculate.lower() == 'r':
    a = float(input('Enter a lenght of the rectangle: \n'))
    b = float(input('Enter a width of the rectangle: \n'))
    print(area.rectangle_area(a, b))
elif calculate.lower() == 't': 
    a = float(input('Enter a lenght of the triangle: \n'))
    b = float(input("Enter a height of the triangle: \n"))
    print(area.triangle_area(a, b))
else:
    print("We dont have this option")