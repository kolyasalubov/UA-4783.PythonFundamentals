
########################################################################## Task1
# class Ball(object):
#     """Doc"""
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

########################################################################## Task2

# from random import randint
# class Ghost:
#     def __init__(self):
#         self.color = randint(1, 4)
#         match self.color:
#             case 1:
#                 self.color = "yellow"
#             case 2:
#                 self.color = "white"
#             case 3:
#                 self.color = "purple"
#             case 4:
#                 self.color = "red"

########################################################################## Task3

# class Human:
#     pass

# class Man(Human):
#         pass
    

# class Woman(Human): 
#         pass

# def God():
#     return Man(), Woman()

########################################################################## Task4

# class Person:
#     def __init__(self,name: str,age: int):
#         self.info = f"{name}s age is {age}"

########################################################################## Task5

# from math import pi
#
# class Sphere:
#     def __init__(self, radius, mass):
#         self.r= radius
#         self.m = mass
        
#     def get_radius(self):
#         return self.r
    
#     def get_mass(self):
#         return self.m
    
#     def get_volume(self):
#         return round((4/3) * pi * self.r**3, 5)
  
#     def get_surface_area(self):
#         return round(4 * pi * self.r**2, 5)
    
#     def get_density(self):
#         V = (4/3) * pi * self.r**3  
#         return round(self.m / V, 5)

########################################################################## Task6

# def class_name_changer(cls, new_name):
#     if new_name.isalnum() and new_name[0].isupper():
#         cls.__name__ = new_name
#     else:
#         raise ValueError("Invalid class name")
