import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
title = pygame.display.set_caption("This is the best game ever")
icon = pygame.image.load('9-03/knight.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Jumping
velocity_y = 5
gravity = 0.10
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
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5
    if keys[pygame.K_SPACE]:
        player.y += 10
        
    velocity_y += gravity
    player.y += velocity_y
    
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