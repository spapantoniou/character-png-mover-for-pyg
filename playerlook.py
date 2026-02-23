import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("gabor")

clock = pygame.time.Clock()

# Load images
player_images = {
    "up": pygame.image.load("gabor_up.png").convert_alpha(),
    "down": pygame.image.load("gabor_down.png").convert_alpha(),
    "left": pygame.image.load("gabor_left.png").convert_alpha(),
    "right": pygame.image.load("gabor_right.png").convert_alpha()
}

current_image = player_images["down"]

# Player rect
player_rect = current_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
speed = 5
direction = "down"

# Game loop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_rect.y -= speed
        direction = "up"
        moving = True
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_rect.y += speed
        direction = "down"
        moving = True
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_rect.x -= speed
        direction = "left"
        moving = True
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_rect.x += speed
        direction = "right"
        moving = True

    # Update sprite
    current_image = player_images[direction]

    # Keep player on screen
    player_rect.x = max(0, min(WIDTH - player_rect.width, player_rect.x))
    player_rect.y = max(0, min(HEIGHT - player_rect.height, player_rect.y))

    # Draw
    screen.fill((30, 30, 30))
    screen.blit(current_image, player_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
