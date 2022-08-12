import pygame
import numpy as np

##pygame.init()

class Particula:
    def __init__(self, pos, rad, masa, ang, rapidez):
        self.pos = pos
        self.rad = rad
        self.masa = masa
        self.ang = ang
        self.u = np.array([[np.cos(self.ang)],
                           [np.sin(self.ang)]])
        self.rapidez = rapidez
        self.v = self.rapidez * self.u

    def display(self):
        pygame.draw.circle(screen, red, self.pos, self.rad, 1)

    def moverse(self):
        self.pos = self.pos + self.v



def choque(partic1, partic2):
    r12 = partic2.pos - partic1.pos
    dist_part12 = np.linalg.norm(r12)
    if dist_part12 <= (partic1.rad + partic2.rad):
        tg = r12 / np.linalg.norm(r12)
        
        




size = (600, 600)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)

part1_pos = np.array([[30],
                      [300]])
part1_rad = 30
part1_masa = 10 #kg
part1_ang = 0 #rad
part1_rapidez = 0.5 #m/s
part1 = Particula(part1_pos, part1_rad, part1_masa, part1_ang, part1_rapidez)

part2_pos = np.array([[500],
                      [300]])
part2_rad = 30
part2_masa = 10 #kg
part2_ang = np.pi #rad
part2_rapidez = 0.5 #m/s
part2 = Particula(part2_pos, part2_rad, part2_masa, part2_ang, part2_rapidez)

R = np.array([[0, -1],
              [1, 0]])

running = True

while running:
    screen.fill(white)
    choque(part1, part2)
    part1.moverse()
    part1.display()
    part2.moverse()
    part2.display()
    pygame.display.flip()





