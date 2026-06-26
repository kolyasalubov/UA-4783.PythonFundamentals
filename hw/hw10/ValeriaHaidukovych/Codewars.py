#Task1

class Ball:
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type



#Task2

import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])



#Task3

class Human(object):
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

Adam = Man()
Eve = Woman()

def God():
    return [Adam, Eve]



#Task4

class Person():
    def __init__(self, name: str, age: int):
        self. name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"



#Task5

import math

class Sphere(object):
    
    def __init__(self, radius: int, mass: int):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        self.v = round(4/3 * math.pi * self.radius ** 3, 5)
        return self.v
    
    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)
    
    def get_density(self):
        return self.mass / self.v
    


#Task6

import re
        
def class_name_changer(cls, new_name):
    if re.match(r"^[A-Z][a-zA-Z0-9]", new_name):
        cls.__name__ = new_name
    else:
        return "Error"
