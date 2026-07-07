from random import randint 

secret_number = randint(1, 100)

for i in range(10):
    user_number = int(input("Enter number range 1-100: "))
    if user_number > secret_number:
        print(" Yor number bigger")
    elif user_number < secret_number:
        print("yor number smaller ")
    else:
        print("You winn!!! ")
        break





