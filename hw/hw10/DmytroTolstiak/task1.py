class Polygon():
    """Базовий клас для багатокутників."""
    def __init__(self, sides: int):
        self.sides = sides

class Rectangle(Polygon):
    """Клас прямокутника."""
    def __init__(self,length: float, width: float):
        super().__init__(sides=4)
        self.length = length
        self.width = width 
        
    @property
    def area(self):
        return self.length * self.width

rect = Rectangle(10,10)

print(rect.sides)
print(rect.length)
print(rect.width)
print(rect.area)
    



