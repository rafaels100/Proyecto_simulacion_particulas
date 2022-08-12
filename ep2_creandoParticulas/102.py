import pygame
import numpy as np

pygame.init()

class Particula:
    def __init__(self, pos, rad):
        self.pos = pos
        self.rad = rad

    def display(self):
        pygame.draw.circle(screen, red, self.pos, self.rad, 1)


width = 600
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)


running = True

##part1_pos = (300, 300)
##part2_pos = (300, 100)
part1_pos = np.array([[300],
                      [300]])
part2_pos = np.array([[300],
                      [100]])


part1 = Particula(part1_pos, 30)
part2 = Particula(part2_pos, 20)

print(part1.pos)

while running:
    screen.fill(white)
    part1.display()
    part2.display()
    pygame.display.flip()
    
    
