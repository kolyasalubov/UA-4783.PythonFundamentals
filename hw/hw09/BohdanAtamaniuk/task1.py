import random


number = int(input("Guess my number!!! (1-100): "))
def guess_number(number):
    random_number = random.randint(1, 100)
    attempt = 1
    while number != random_number and attempt < 10:
        print(f"Attempt {attempt} of 10")
        if number < random_number:
            number = int(input("Too low! Try again: \n"))
        elif number > random_number:
            number = int(input("Too high! Try again: \n"))

        attempt += 1
    if not random_number == number:
        return("U dont have any try")

    return(f"Well done is was {random_number}")
    
    

print(guess_number(number))
