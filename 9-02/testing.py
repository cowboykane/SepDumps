import pygame 

# Initial Setup: display, clock

pygame.init()


screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("This is just 2 squares")
icon = pygame.image.load('9-02/cloud.jpg')
pygame.display.set_icon(icon)

# Objects: 2 players

player1 = pygame.Rect(100, 100, 40, 40) # x, y, width, height
player2 = pygame.Rect(350, 100, 40, 40) # x, y, width, height

# Running Loop 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    
    old_x1, old_y1 = player1.x, player1.y
    old_x2, old_y2 = player2.x, player2.y
    
    # Key bindings 
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.x -= 5
    if keys[pygame.K_a]:
        player2.x -= 5
        
    if keys[pygame.K_RIGHT]:
        player1.x += 5
    if keys[pygame.K_d]:
        player2.x += 5
        
    if keys[pygame.K_UP]:
        player1.y -= 5
    if keys[pygame.K_w]:
        player2.y -= 5
        
    if keys[pygame.K_DOWN]:
        player1.y += 5
    if keys[pygame.K_s]:
        player2.y += 5
        
    # Collision Check 
    if player1.colliderect(player2):
        player1.x, player1.y = old_x1, old_y1
        player2.x, player2.y = old_x2, old_y2
    
    # Display objects, clock tick
    
    pygame.draw.rect(screen, ("#F54927"), player1) 
    pygame.draw.rect(screen, ("#2735F5"), player2)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()