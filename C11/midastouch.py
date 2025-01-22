import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Player Control and Collision")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Set up player and square properties
PLAYER_SIZE = 50
SQUARE_SIZE = 50
player_x, player_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
player_speed = 5

square_x = random.randint(0, WINDOW_WIDTH - SQUARE_SIZE)
square_y = random.randint(0, WINDOW_HEIGHT - SQUARE_SIZE)
square_color = RED

# Create clock object
FPS = 30
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - PLAYER_SIZE:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - PLAYER_SIZE:
        player_y += player_speed

    # Check for collision between player and square
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    square_rect = pygame.Rect(square_x, square_y, SQUARE_SIZE, SQUARE_SIZE)
    if player_rect.colliderect(square_rect):
        square_color = GOLD

    # Draw the screen
    display_surface.fill(WHITE)  # Clear the screen
    pygame.draw.rect(display_surface, BLUE, player_rect)  # Draw player
    pygame.draw.rect(display_surface, square_color, square_rect)  # Draw square

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)  # Maintain frame rate

# Quit pygame
pygame.quit()
