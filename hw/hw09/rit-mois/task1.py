from random import randint


secret_number = randint(1, 100)

print("You have 10 attempts to guess a number from 1 to 100.")

for attempt in range(1, 11):
    guess = int(input(f"\nAttempt {attempt}/10. Enter your number: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempt} attempts!")
        break
    elif guess < secret_number:
        print("The secret number is greater.")
    else:
        print("The secret number is less.")
else:
    print(f"\nYou have used all 10 attempts.")
    print(f"The secret number was {secret_number}. Better luck next time!")