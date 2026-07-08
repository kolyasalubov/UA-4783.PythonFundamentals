def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            elif age % 2 == 0:
                print("Your age is even.")
            else:
                print("Your age is odd.")
            break
        except ValueError as e:
            print(f"Error: {e}")
            return get_age()
        
get_age()