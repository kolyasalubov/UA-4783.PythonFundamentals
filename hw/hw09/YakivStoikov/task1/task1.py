import sys
from random import randint
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Number Guessing Game")

COLOR_BG = (240, 244, 248)
COLOR_PRIMARY = (33, 150, 243)
COLOR_TEXT = (44, 62, 80)
COLOR_SUCCESS = (46, 204, 113)
COLOR_FAIL = (231, 76, 60)
COLOR_BOX = (255, 255, 255)

font_title = pygame.font.SysFont("Arial", 40, bold=True)
font_body = pygame.font.SysFont("Arial", 24)
font_input = pygame.font.SysFont("Arial", 32, bold=True)

secret_number = randint(1, 100)
max_attempts = 10
attempts_used = 0
user_text = ""
feedback_message = "Enter a number between 1 and 100 and press ENTER"
game_over = False
won = False

input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 40, 200, 50)

clock = pygame.time.Clock()

while True:
    for event in pygame.get_poly_events() if hasattr(pygame, 'get_poly_events') else pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_RETURN:
                    if user_text.strip().isdigit():
                        guess = int(user_text)
                        attempts_used += 1

                        # Check guess rules
                        if guess == secret_number:
                            feedback_message = f"Congratulations! You guessed it in {attempts_used} tries!"
                            won = True
                            game_over = True
                        elif attempts_used >= max_attempts:
                            feedback_message = f"Game Over! The number was {secret_number}."
                            game_over = True
                        elif guess < secret_number:
                            feedback_message = f"The secret number is GREATER than {guess}."
                        else:
                            feedback_message = f"The secret number is LESS than {guess}."
                    else:
                        feedback_message = "Please enter a valid number!"

                    user_text = "" 

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 3 and event.unicode.isdigit():
                        user_text += event.unicode

    screen.fill(COLOR_BG)

    title_surface = font_title.render(
        "Guess the Secret Number", True, COLOR_PRIMARY
    )
    screen.blit(
        title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 50)
    )

    attempts_surface = font_body.render(
        f"Attempts remaining: {max_attempts - attempts_used}", True, COLOR_TEXT
    )
    screen.blit(
        attempts_surface,
        (SCREEN_WIDTH // 2 - attempts_surface.get_width() // 2, 130),
    )

    pygame.draw.rect(screen, COLOR_BOX, input_rect, border_radius=8)
    pygame.draw.rect(screen, COLOR_PRIMARY, input_rect, 3, border_radius=8)

    text_surface = font_input.render(user_text, True, COLOR_TEXT)
    screen.blit(
        text_surface,
        (
            input_rect.x + (input_rect.width - text_surface.get_width()) // 2,
            input_rect.y + (input_rect.height - text_surface.get_height()) // 2,
        ),
    )

    if game_over:
        msg_color = COLOR_SUCCESS if won else COLOR_FAIL
    else:
        msg_color = COLOR_TEXT

    feedback_surface = font_body.render(feedback_message, True, msg_color)
    screen.blit(
        feedback_surface,
        (SCREEN_WIDTH // 2 - feedback_surface.get_width() // 2, 400),
    )

    if game_over:
        reset_surface = font_body.render(
            "Close the window to exit.", True, COLOR_TEXT
        )
        screen.blit(
            reset_surface,
            (SCREEN_WIDTH // 2 - reset_surface.get_width() // 2, 480),
        )

    pygame.display.flip()
    clock.tick(60)