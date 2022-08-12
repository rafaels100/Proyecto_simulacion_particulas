import pygame
import numpy as np

##pygame.init()

class Particula:
    def __init__(self, pos, rad, masa):
        self.pos = pos
        self.rad = rad
        self.masa = masa

    def display(self):
        pygame.draw.circle(screen, red, self.pos, self.rad, 1)




size = (600, 600)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)

##part1_pos = (300, 300)

part1_pos = np.array([[300],
                      [300]])
part1_rad = 30
part1_masa = 10 #kg
part1 = Particula(part1_pos, part1_rad, part1_masa)

running = True



while running:
    screen.fill(white)
    part1.display()
    print(part1.masa)
    pygame.display.flip()





