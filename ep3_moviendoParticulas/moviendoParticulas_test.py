import pygame
import numpy as np

##pygame.init()

class Particula:
    def __init__(self, pos, rad, masa, ang, rapidez):
        self.pos = pos
        self.rad = rad
        self.masa = masa
        self.rapidez = rapidez
        self.u = np.array([[np.cos(ang)],
                           [np.sin(ang)]])
        #v = mod_v * versor_v
        self.v = self.rapidez * self.u
        
        

    def display(self):
        pygame.draw.circle(screen, red, self.pos, self.rad, 1)

    def avanzar(self):
        self.pos[0] = self.pos[0] + 1

    def retroceder(self):
        self.pos[0] = self.pos[0] - 1

    def subir(self):
        self.pos[1] = self.pos[1] - 1

    def bajar(self):
        self.pos[1] = self.pos[1] + 1

    def diagonal(self):
        self.pos = self.pos + self.v
        



size = (600, 600)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)

##part1_pos = (300, 300)

part1_pos = np.array([[300],
                      [300]])
part1_rad = 30
part1_masa = 10 #kg
part1_ang = 0 #rad
part1_rapidez = 3 #m/s
part1 = Particula(part1_pos, part1_rad, part1_masa, part1_ang, part1_rapidez)

running = True



while running:
    screen.fill(white)
    part1.diagonal()
    part1.display()
##    print(part1.masa)
    pygame.display.flip()





