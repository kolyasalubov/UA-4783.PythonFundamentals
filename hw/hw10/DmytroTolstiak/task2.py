class Human:
    """Клас людини"""
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello {self.name}!"
    
    @classmethod
    def species(cls):
        return "Homo Sapiens"
    
    @staticmethod
    def message():
        return "Smtg*&^%"

dima = Human("Dmytro")

print(dima.say_hello())
print(Human.species())
print(Human.message())
