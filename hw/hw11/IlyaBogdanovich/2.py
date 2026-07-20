def week(number):
    try:
        if not number.isdigit():
            raise Exception
        number = int(number)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[number - 1]
    except Exception:
        return "Wrong data input!"
number = input("Enter your number: ")
print(week(number))

