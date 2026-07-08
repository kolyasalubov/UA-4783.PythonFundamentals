from random import randint

print("Guess a randomly generated number from a range of 1 to 100!\nYou have 10 attempts!")
number = randint(1, 100)

for count in range(0, 10):
    guess = int(input("Input your guess!\n"))
    if guess == number:
        print("Congratulations, you won!")
        break
    if guess > number:
        print("The number is less than your input!")
    else:
        print("The number is greater than your input!")
else:
    print("All 10 attempts have been exhausted, you lost!")
