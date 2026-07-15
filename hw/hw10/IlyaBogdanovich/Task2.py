class Human:
    def __init__(self, name):
        self.names = name

    def welcome_message(self):
            print(f"Welcome, {self.name}!")

    def species(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        print("I love Python")

