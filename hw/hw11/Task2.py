week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def number_to_day(num):
    try:
        number = int(num)
        if number >= 1:
            return week[number - 1]
        else:
            raise IndexError
    except IndexError:
        return "Error, that number is incorrect"
    except ValueError:
        return "Non numerical data"
