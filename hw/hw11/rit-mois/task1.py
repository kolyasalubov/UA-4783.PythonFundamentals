class InputError(Exception):
    """Raised when user enters a negative number."""


def check_age_even_odd(age):
    if age <= 0:
        raise InputError("Age cannot be negative or 0.")

    if age % 2 == 0:
        return "The age is even."

    return "The age is odd."


def check_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            print(check_age_even_odd(age))
            break

        except ValueError:
            print("Please enter a valid integer.")

        except InputError as error:
            print(error)


check_age()
