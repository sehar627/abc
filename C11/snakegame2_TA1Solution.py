import pygame
import random
# Initialize pygame
pygame.init()

# Set up display
WINDOW_WIDTH=600
WINDOW_HEIGHT=600

#Set game values
SNAKE_SIZE = 20
APPLE_SIZE=20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
pick_up_sound = pygame.mixer.Sound("C:/Users/pc/Desktop/python/Pygames/pick_up_sound.wav")


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detect window close
            running = False

    
    # Fill the screen with a white background
    display.fill((255, 255, 255))
    
    pygame.draw.rect(display,"green",(250,250,SNAKE_SIZE,SNAKE_SIZE))
    # Update display
    pygame.display.flip()
   
pygame.quit()
