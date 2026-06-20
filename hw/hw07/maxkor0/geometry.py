def main():
    figure = input("Choose: rectangle, triangle, circle. ").casefold()
    figures = ["rectangle", "triangle", "circle"]
    while figure not in figures:
        figure = input("Invalid choice. Try again: ").casefold()

    if figure == "rectangle":
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        print(rectangle_area(l, w))
    elif figure == "triangle":
        b = int(input("Enter base: "))
        h = int(input("Enter height: "))
        print(triangle_area(b, h))
    elif figure == "circle":
        r = int(input("Enter radius: "))
        print(circle_area(r))


def rectangle_area(l, w):
    """Calculates rectangle area"""
    return l * w
  

def triangle_area(b, h):
    """Calculates triangle area"""
    return (b * h) / 2

def circle_area(r):
    """Calculates circle area"""
    return 3.14 * r ** 2

main()
