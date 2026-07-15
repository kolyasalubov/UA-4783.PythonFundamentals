class Polygon:
    def __init__(self, number_of_sides):
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: "))
                                            for i in range(self.n)]
        

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def inputSides(self):
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        self.sides = [length, width, length, width]

    def findArea(self):
        a, b = self.sides[:2]
        area = a * b
        print(f"The area of the triangle is {area}")