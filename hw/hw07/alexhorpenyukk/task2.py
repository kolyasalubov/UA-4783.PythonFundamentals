'''
Task2 Write a program that calculates the area of a rectangle, triangle and circle 
(write three functions to calculate the area. And call them in the main program depending on the user's choice).
'''

import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 2 * math.pi * radius ** 2

choise = input('Which area do you want to calculate? (rectangle / triangle / circle): ')

if choise == 'rectangle':
    length = float(input('length = '))
    width = float(input('width = '))
    print(f'The area = {round(rectangle_area(length, width), 1)}')
elif choise == 'triangle':
    base = float(input('base = '))
    height = float(input('height = '))
    print(f'The area = {round(triangle_area(base, height), 1)}')
elif choise == 'circle':
    radius = float(input('radius = '))
    print(f'The area = {round(circle_area(radius), 1)}')
