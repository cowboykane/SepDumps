import pygame 
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
        self.clock = pygame.time.Clock() # Control framerate
        pygame.display.set_caption("Woahhhh")

    def run(self):
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        
        
        pygame.display.update()
        self.clock.tick(60) # Runs the game at 60 fps

Game().run()