def get_day():
    while True:
        try:
            day = int(input("Enter a day of the week (1-7): "))
            match day:
                case 1:
                    return "Monday"
                case 2:
                    return "Tuesday"
                case 3:
                    return "Wednesday"
                case 4:
                    return "Thursday"
                case 5:
                    return "Friday"
                case 6:
                    return "Saturday"
                case 7:
                    return "Sunday"
                case _:
                    raise ValueError("Invalid day number.") 
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

print(get_day())
