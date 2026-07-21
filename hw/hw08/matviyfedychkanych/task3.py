from task3_modules import rectangle_area, triangle_area, circle_area

print("We have 3 figure to choise: ")
print("1 - rectangle")
print("2 - triangle")
print("3 - circle")
figure = input("Enter your choise: ")

if figure == "1":
    a = float(input("Your lenght: "))
    b = float(input("Your width: "))
    print(f"Your rectangle area: {rectangle_area(a, b)}")
elif figure == "2":
    h = float(input("Your height: "))
    a = float(input("Your base: "))
    print(f"Your triangle area: {triangle_area(h, a)}")
elif figure == "3":
    r = float(input("Your radius: "))
    print(f"Your circle area: {circle_area(r)}")
else:
    print("Incorrect choise or figure")