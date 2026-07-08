'''Regular Ball Super Ball'''
class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


'''Color Ghost'''
from random import choice

class Ghost:
    colors = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = choice(self.colors)


'''Basic subclasses - Adam and Eve'''
def God():
    return [Man(), Woman()]

class Human:
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass


'''Classy Classes'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    

'''Building Spheres'''
from math import pi

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return 4/3 * pi * self.radius ** 3
    
    def get_surface_area(self):
        return 4 * pi * self.radius ** 2
    
    def get_density(self):
        return self.mass / self.get_volume()

    

'''Python's Dynamic Classes #1'''
import re

def class_name_changer(cls, new_name):
    if not re.fullmatch(r'[A-Z][a-zA-Z0-9]*', new_name):
        raise Exception('Invalid class name')

    cls.__name__ = new_name
    return cls
