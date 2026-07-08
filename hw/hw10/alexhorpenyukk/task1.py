class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
class Rectangle(Polygon):
    def __init__(self, sides, width, height):
        super().__init__(sides)
        self.width = width
        self.height = height
    
    def square(self):
        return self.width * self.height
    