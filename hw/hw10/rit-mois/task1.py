class Polygon:
    def __init__(self):
        self.width = self._input_validation("Enter width of polygon: ")
        self.height = self._input_validation("Enter height of polygon: ")

    def _input_validation(self, message):
        while True:
            try:
                side = float(input(message))

                if side <= 0:
                    print("The value must be greater than 0")
                    continue

                return side
            except ValueError:
                print("Please enter a number")


class Rectangle(Polygon):
    def square(self):
        return self.width * self.height


rect = Rectangle()
print(f"Rectangle square: {rect.square()}")
