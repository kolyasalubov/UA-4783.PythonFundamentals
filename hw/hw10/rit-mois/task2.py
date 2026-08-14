class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f'Welcome, {self.name}!')

    @classmethod
    def species(cls):
        return 'Homosapiens'

    @staticmethod
    def arbitrary_message():
        return 'This is an arbitrary message.'


person1 = Human('Rita')
person1.welcome()

print(person1.species())
print(person1.arbitrary_message())

print(Human.species())
print(Human.arbitrary_message())
