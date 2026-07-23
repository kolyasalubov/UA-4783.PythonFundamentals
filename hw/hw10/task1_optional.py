class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def __init__ (self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

length = float(input("Write your length of rectangle: "))
width = float(input("Write your width of rectangle: "))

my_rect = Rectangle(length, width)
print(f"Your square: {my_rect.area()}")
