import pygame
import random
import random
# Initialize pygame
pygame.init()

# Set up display
WINDOW_WIDTH=600
WINDOW_HEIGHT=600


#Set game values
SNAKE_SIZE = 20
APPLE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2

snake_dx = 0
snake_dy = 0

score = 0

FPS=30
clock=pygame.time.Clock()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
pick_up_sound = pygame.mixer.Sound("C:/Users/pc/Desktop/Rigel Infotech/c11/C11/pick_up_sound.wav")

apple_coord = (500, 500, APPLE_SIZE, APPLE_SIZE)
apple_rect = pygame.draw.rect(display,"red", apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display, "green", head_coord)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detect window close
            running = False

        #Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1*SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1*SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    if head_rect.colliderect(apple_rect):
        pick_up_sound.play()

    
    # Fill the screen with a white background
    display.fill((255, 255, 255))
    
    head_rect = pygame.draw.rect(display, "green", head_coord)
    apple_rect = pygame.draw.rect(display, "red", apple_coord)

    for i in range(10):
        rect_x = random.randint(0, WINDOW_WIDTH - 30)
        rect_y = random.randint(0, WINDOW_HEIGHT - 30)
        pygame.draw.rect(display, "blue", (rect_x, rect_y, 30, 30))
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
   
pygame.quit()
