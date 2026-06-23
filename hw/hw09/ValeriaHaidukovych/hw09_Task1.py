import random

number = random.randint(1, 100)
counter = 0
result = f"Game over! Guessed number was {number}"
while counter <= 10:
    user_number = int(input())
    if user_number == number:
        result = "You win!"
        break
    elif user_number > number:
        print("Guessed number is less")
    elif user_number < number:
        print("Guessed number is greater")
    counter += 1
print(result)