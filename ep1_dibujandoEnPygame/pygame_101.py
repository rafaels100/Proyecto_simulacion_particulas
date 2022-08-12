import pygame

pygame.init()

class Particula:
    def __init__(self, pos, rad):
        self.pos = pos
        self.rad = rad

    def display(self):
        pygame.draw.circle(screen, self.pos, self.rad)


width = 600
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)


running = True


while running:
    screen.fill(white)
    pygame.display.flip()
    
    
