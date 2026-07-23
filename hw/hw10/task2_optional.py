class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello {self.name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "It's my arbitrary message"