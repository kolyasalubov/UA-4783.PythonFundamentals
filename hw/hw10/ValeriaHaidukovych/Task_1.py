class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def input_sides(self):
        for i in range(self.num_of_sides):
            self.sides[i] = float(input("Enter side:"))
        

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def find_square(self):
        a = b = None
        for i in self.sides:
            if a == None:
                a = i
            elif a == i:
                continue
            else:
                b = i

        square = a * b
        print(f"The square of the rectangle is {square}")
