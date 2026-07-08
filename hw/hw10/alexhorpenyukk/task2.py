class Human:
    species = 'Homosapiencs'

    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f'Welcome {self.name}'
    
    @classmethod
    def spec(cls):
        return f'Human is a {cls.species}'
    
    @staticmethod
    def arbitrary_message():
        return 'Hello world'