import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Guess the number")
font = pygame.font.Font(None, 36)
font_large = pygame.font.Font(None, 44)

number = randint(1, 101)
attempts = 10
user_input = ""
message = ""
guesses_left = attempts

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.isdigit():
                    guess = int(user_input)
                    if guess < number:
                        message = "Too low! Try again."
                    elif guess > number:
                        message = "Too high! Try again."
                    else:
                        message = f"Correct! You guessed the number. It was {number}."
                        screen.fill((40, 40, 40))
                        msg_text = font_large.render(message, True, (0, 255, 0))
                        screen.blit(msg_text, (65, 180))
                        pygame.display.flip()  
                        pygame.time.wait(3000)  
                        running = False
                    guesses_left -= 1
                    if guesses_left == 0 and guess != number:
                        message = f"You've run out of attempts! The number was {number}."
                        screen.fill((40, 40, 40))
                        msg_text = font_large.render(message, True, (255, 0, 0))
                        screen.blit(msg_text, (55, 180))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                    user_input = ""
                else:
                    message = "Please enter a valid number."
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode
    if not running:
        break

    screen.fill((40, 40, 40))

    title = font.render("Guess the number (1-100)", True, (255, 255, 255))
    screen.blit(title, (50, 50))

    attempts_text = font.render(f"Attempts left: {guesses_left}", True, (255, 255, 0))
    screen.blit(attempts_text, (50, 100))

    input_text = font.render(f"Your guess: {user_input}", True, (255, 255, 255))
    screen.blit(input_text, (50, 200))

    msg_text = font.render(message, True, (0, 255, 0))
    screen.blit(msg_text, (50, 300))

    pygame.display.flip()

pygame.quit()