import pygame

# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = 600
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit the game
            running = False

    # Fill the screen with a white background
    display.fill(WHITE)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
