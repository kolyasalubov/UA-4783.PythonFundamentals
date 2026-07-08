import random

secret_number = random.randint(1, 100)

print("Guess the number from 1 to 100.")
print("You have 10 attempts.")

for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("The hidden number is greater.")
    else:
        print("The hidden number is less.")
else:
    print("You have used all 10 attempts.")
    print(f"The hidden number was {secret_number}.")