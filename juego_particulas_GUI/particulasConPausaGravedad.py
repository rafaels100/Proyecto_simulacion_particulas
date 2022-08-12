import pygame
import numpy as np
import random

##pygame.init()
def run(masa1, masa2, size1, size2):
    class Particula:
        def __init__(self, pos, rad, masa, ang, rapidez):
            self.pos = pos
            self.rad = rad
            self.m = masa
            self.ang = ang
            self.u = np.array([[np.cos(self.ang)],
                               [np.sin(self.ang)]])
            self.rapidez = rapidez
            self.v = self.rapidez * self.u
            self.a = np.array([[0],
                               [0]])

        def display(self):
            pygame.draw.circle(screen, red, (self.pos[0][0],
                                             self.pos[1][0]), self.rad, 1)

        def moverse(self):
            self.pos = self.pos + self.v

        def rebotar(self):
            if self.pos[0] > (size[0] - self.rad):
                self.v[0] = -self.v[0]
            elif self.pos[0] < self.rad:
                self.v[0] = -self.v[0]
            if self.pos[1] > (size[1] - self.rad):
                self.v[1] = -self.v[1]
            elif self.pos[1] < self.rad:
                self.v[1] = -self.v[1]



    def choque(partic1, partic2):
        r12 = partic2.pos - partic1.pos
        dist_part12 = np.linalg.norm(r12)
        if dist_part12 <= (partic1.rad + partic2.rad):
            tg = r12 / np.linalg.norm(r12)
            n = np.dot(R, tg)
            rapi1tg_ia = np.dot(partic1.v.T, tg)
            rapi1n_ia = np.dot(partic1.v.T, n)
            rapi2tg_ia = np.dot(partic2.v.T, tg)
            rapi2n_ia = np.dot(partic2.v.T, n)
            rapi1tg_id = (2 * partic2.m / (partic1.m + partic2.m)) * rapi2tg_ia + \
                         ((partic1.m - partic2.m) / (partic1.m + partic2.m)) * rapi1tg_ia
            rapi2tg_id = (2 * partic1.m / (partic1.m + partic2.m)) * rapi1tg_ia + \
                         ((partic2.m - partic1.m) / (partic1.m + partic2.m)) * rapi2tg_ia
            rapi1n_id = rapi1n_ia
            rapi2n_id = rapi2n_ia
            partic1.v = rapi1tg_id * tg + rapi1n_id * n
            partic2.v = rapi2tg_id * tg + rapi2n_id * n
            partic1.pos = partic1.pos + partic1.v * 0.1
            partic2.pos = partic2.pos + partic2.v * 0.1
            
    def g():
        #el campo gravitatorio g es constante en cada punto
        #el modulo del campo es
        mod_g = 0.2 #m/s**2
        #el campo g siempre apunta hacia el centro de la Tierra
        u = np.array([[0],
                      [1]])
        g = mod_g * u
        #el valor del campo g en el punto es
        return g

    def P(obj):
        #el peso de un objeto es igual a la masa inercial de dicho objeto
        #multiplicado por el campo gravitatorio g
        P = obj.m * g()
        return P

    def sum_F(obj):
        sum_F = P(obj)
        #La segunda ley de Newton nos dice que
        #Sum_F = m * a
        obj.a = sum_F / obj.m
        #Utilizando el metodo de Euler Crommer puedo calcular la velocidad del
        #objeto sometido a estas fuerzas
        #dv / dt = a
        #Pero no necesitamos infinitesimales, conque sea lo suficientemente
        #pequeño para una buena aproximacion nos alcanza
        #delta_v / delta_t = a
        #(vf - vi) = a * delta_t
        #vf = vi + a * delta_t
        obj.v = obj.v + obj.a * dt
        """
        NOTA: Este dt lo tomamos tan pequeño como nosotros querramos. Mientras mas
        pequeño, mejor nuestra aproximacion, pero mas tardara en realizar los
        calculos el programa. No es un dt como tal porque no es infinitamente
        pequeño, pero a efectos del programa lo podemos considerar como que si.
        """
                   
    def pause():
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
            




    size = (600, 600)
    screen = pygame.display.set_mode(size)
    white = (255, 255, 255)
    red = (255, 0, 0)
    
    part1_pos = np.array([[random.randint(0,500)],
                          [random.randint(0,500)]])
    part1_rad = size1
    part1_masa = masa1 #kg
    part1_ang = 0 #rad
    part1_rapidez = 0.06 #m/s
    part1 = Particula(part1_pos, part1_rad, part1_masa, part1_ang, part1_rapidez)

    part2_pos = np.array([[random.randint(0,500)],
                          [random.randint(0,500)]])
    part2_rad = size2
    part2_masa = masa2 #kg
    part2_ang = np.pi #rad
    part2_rapidez = 0.08 #m/s
    part2 = Particula(part2_pos, part2_rad, part2_masa, part2_ang, part2_rapidez)

    R = np.array([[0, -1],
                  [1, 0]])

    dt = 0.01

    particulas = [part1, part2]

    running = True


    while running:
        screen.fill(white)
        for part in particulas:
            sum_F(part)
            part.moverse()
            part.rebotar()
            part.display()
        choque(part1, part2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()





