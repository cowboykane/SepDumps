import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
title = pygame.display.set_caption("This is the best game ever")
icon = pygame.image.load('9-03/knight.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Jumping
velocity_y = 5
gravity = 0.5
is_grounded = False

player = pygame.Rect(50, 50, 40, 40)
floor = pygame.Rect(0, 450, 1500, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_SPACE] and is_grounded:
        velocity_y = -10
        
    velocity_y += gravity
    player.y += velocity_y
    
    is_grounded = False
    
    if player.colliderect(floor):
        if velocity_y > 0:
            player.bottom = floor.top
            velocity_y = 0
            is_grounded = True

    
    pygame.draw.rect(screen, ("#96A211"), player)
    pygame.draw.rect(screen, ("#792C75"), floor)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()