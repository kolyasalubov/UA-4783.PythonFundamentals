import areas_module

figure = input('Area of which figure do you want to calculate? (rectangle / triangle / circle): ')

if figure == 'rectangle':
    length = float(input('length = '))
    width = float(input('width = '))
    print(f'The area = {round(areas_module.rectangle_area(length, width), 1)}')
elif figure == 'triangle':
    base = float(input('base = '))
    height = float(input('height = '))
    print(f'The area = {round(areas_module.triangle_area(base, height), 1)}')
elif figure == 'circle':
    radius = float(input('radius = '))
    print(f'The area = {round(areas_module.circle_area(radius), 1)}')