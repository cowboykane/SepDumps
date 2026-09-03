import pygame 

pygame.init()
screen = pygame.display.set_mode((400, 300), pygame.RESIZABLE)
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 40, 40)

wall = pygame.Rect(200, 100, 60, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5
    
    if player.colliderect(wall):
        print("Collision detected!")
    
    
    screen.fill(("black"))       
    pygame.draw.rect(screen, (255, 100, 100), player) # x, y, width, height
    pygame.draw.rect(screen, (100, 200, 200), wall)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()