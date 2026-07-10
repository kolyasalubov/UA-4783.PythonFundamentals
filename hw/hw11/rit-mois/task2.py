class DayError(Exception):
    """Raised when the entered number is not between 1 and 7."""


DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def get_day(number):
    if number not in DAYS:
        raise DayError("Please enter a number from 1 to 7.")

    return DAYS[number]


def number_to_day():
    while True:
        try:
            number = int(input("Enter a number of the day (1-7): "))
            print(get_day(number))
            break

        except ValueError:
            print("Please enter a valid integer.")

        except DayError as error:
            print(error)


number_to_day()
