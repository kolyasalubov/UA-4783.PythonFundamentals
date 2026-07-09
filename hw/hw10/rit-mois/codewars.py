# Regular Ball Super Ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Color Ghost
import random


class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = random.choice(Ghost.colors)


# Basic subclasses - Adam and Eve
class Human:
   def __init__(self, name):
      self.name = name

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man("Adam"), Woman("Eva")]


# Classy Classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# Building Spheres
from math import pi


class Sphere:
    def __init__(self, radius: int | float, mass: int | float):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4 / 3) * pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)

    def get_density(self):
        volume = (4 / 3) * pi * self.radius ** 3
        return round(self.mass / volume, 5)


# Dynamic Classes
def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name
