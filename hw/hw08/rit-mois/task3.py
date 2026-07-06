from task3_areas import rectangle, triangle, circle


choice = input("Choose екa figure (rectangle, triangle, circle): ").lower()

match choice:
    case "rectangle":
        a = float(input("Enter length: "))
        b = float(input("Enter width: "))
        print(f"Area = {rectangle(a, b)}")

    case "triangle":
        a = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area = {triangle(a, h)}")

    case "circle":
        r = float(input("Enter radius: "))
        print(f"Area = {circle(r)}")

    case _:
        print("Invalid choice!")
