from random import randint

guessed_number = randint(1, 100)
tries = 10
user_number = None

while not user_number == guessed_number:
    if tries == 0:
        print(f'У вас закінчилися спроби \nЗагадане число було {guessed_number}')
        break

    user_number = int(input('Введіть число від 1 до 100: '))
    if user_number < guessed_number:
        print(f'Загадане число більше за {user_number}')
    elif user_number > guessed_number:
        print(f'Загадане число менше за {user_number}')
    else:
        print(f'Ви вгадали, загадане число було {guessed_number}')
        break
    tries -= 1
