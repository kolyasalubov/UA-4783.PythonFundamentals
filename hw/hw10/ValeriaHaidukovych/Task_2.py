class Human:
    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        print(f"Hello, {self.name}")

    @classmethod
    def class_method(cls):
        return "It is a species of Homosapiens"
    
    @staticmethod
    def static_method():
        return "This is Human"
