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
        #calculo el versor que une a las dos particulas. Lo llamo tangente
        tg = r12 / np.linalg.norm(r12)
        #calculo el versor normal al movimiento de la particula 1
        #Como tg ya es un versor, su rotacion tambien lo es
        n = np.dot(R, tg)
        #calculo la proyeccion de la velocidad de la particula 1 sobre
        #el versor tangente, que une a las dos particulas
        rapi1tg_ia = np.dot(partic1.v.T, tg)
        #calculo la proyeccion de la velocidad de la particula 1 sobre
        #el versor normal al que une a las dos particulas
        rapi1n_ia = np.dot(partic1.v.T, n)
        #calculo la proyeccion de la velocidad de la particula 2 sobre
        #el versor tangente, que une a las dos particulas
        rapi2tg_ia = np.dot(partic2.v.T, tg)
        #calculo la proyeccion de la velocidad de la particula 2 sobre
        #el versor normal al que une a las dos particulas
        rapi2n_ia = np.dot(partic2.v.T, n)
        #Utilizando las ecuaciones del choque elastico, calculo la rapidez
        #final tangencia de la particula 1 y 2
        rapi1tg_id = (2*partic2.masa/(partic1.masa+partic2.masa))*rapi2tg_ia + \
                     ((partic1.masa-partic2.masa)/(partic1.masa+partic2.masa))*rapi1tg_ia
        rapi2tg_id = (2*partic1.masa/(partic1.masa+partic2.masa))*rapi1tg_ia + \
                     ((partic2.masa-partic1.masa)/(partic1.masa+partic2.masa))*rapi2tg_ia
        #Calculo las velocidades finales normales de la particula 1 y 2
        rapi1n_id = rapi1n_ia
        rapi2n_id = rapi2n_ia
        #Calculo las velocidades finales de la particula 1 y 2
        partic1.v = rapi1tg_id * tg + rapi1n_id * n
        partic2.v = rapi2tg_id * tg + rapi2n_id * n
        #Actualizo las rapideces finales
        partic1.rapi = np.linalg.norm(partic1.v)
        partic2.rapi = np.linalg.norm(partic2.v)
        #aumento ligeramente la posicion de las particulas en la direccion
        #de las nuevas velocidades, para evitar superposiciones
        partic1.pos += partic1.v * 0.1
        partic2.pos += partic2.v * 0.1
        
        
        
        
        
        
    



size = (600, 600)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)

##partic1_pos = (300, 300)

part1_pos = np.array([[30],
                      [270]])
part1_rad = 30
part1_masa = 10 #kg
part1_ang = 0 #rad
part1_rapidez = 0.2 #m/s
part1 = Particula(part1_pos, part1_rad, part1_masa, part1_ang, part1_rapidez)

part2_pos = np.array([[500],
                      [300]])
part2_rad = 30
part2_masa = 10 #kg
part2_ang = np.pi #rad
part2_rapidez = 0.1 #m/s
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





