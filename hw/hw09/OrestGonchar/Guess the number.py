import random
import random
number = random.randint(1,100)
for n in range(10):
    user = int(input("Enter number"))
    if user == number:
        print("Congratulations!")
        break
    elif user < number:
        print("Secret number is bigger.")
    else:
        print("Secret number is smaller.")
else:
    print(f"You lose! Secret number: {number}")