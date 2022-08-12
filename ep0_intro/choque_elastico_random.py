import pygame
import numpy as np
import random

class Particula:
    def __init__(self, posicion, radio, rapidez, ang, masa):
        self.posicion = posicion
        self.posicion_0 = posicion
        self.posicion_0_dist = posicion
        self.radio = radio
        self.rapidez = rapidez
        #se crea el versor velocidad
        self.u = np.array([[np.cos(ang)],
                           [np.sin(ang)]])
        #se crea el vector velocidad
        self.v = self.u * self.rapidez
        self.masa = masa
        self.p = self.v * self.masa
        self.a = np.array([[0],
                           [0]])
        self.dist = 0
        self.dl = np.array([[0],
                            [0]])
        self.w_inst = 0
        self.w_tot = 0

    def moverse(self):
        #Al multiplicar por 10 estoy indicando que 1m = 10px
        self.posicion = self.posicion + self.v * dt * 10

    def display(self):
        pygame.draw.circle(screen, blue, (int(self.posicion[0]),
                                         int(self.posicion[1])), self.radio, 1)

    def vect_display(self, F):
        pygame.draw.line(screen, red, self.posicion, self.posicion + F)
    
    def rebotar(self):
        if self.posicion[0] > (width - self.radio):
            self.v[0] = -self.v[0]
            self.v[0] = self.v[0]
        elif self.posicion[0] < self.radio:
            self.v[0] = -self.v[0]
            self.v[0] = self.v[0]
        if self.posicion[1] > (height - self.radio):
            self.v[1] = -self.v[1]
            self.v[1] = self.v[1]
        elif self.posicion[1] < self.radio:
            self.v[1] = -self.v[1]
            self.v[1] = self.v[1]

    def dist_rec(self):
        self.dl = self.posicion_0_dist - self.posicion
        self.dist = self.dist + np.linalg.norm(self.dl)
        self.posicion_0_dist = self.posicion

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

def choque_elast(part1, part2):
    dist_part12 = np.linalg.norm(part2.posicion - part1.posicion)
    if dist_part12 < (part1.radio + part2.radio):
        tg = part1.posicion - part2.posicion
        tg = tg / np.linalg.norm(tg)
        n = np.dot(R, tg)
        rapi1tg = np.dot(part1.v.T, tg)
        rapi1n = np.dot(part1.v.T, n)
        rapi2tg = np.dot(part2.v.T, tg)
        rapi2n = np.dot(part2.v.T, n)
        part1.rapi = (part1.masa * rapi1tg - part2.masa * rapi1tg + 2 * part2.masa * rapi2tg)/(part1.masa + part2.masa)
        part2.rapi = (2 * part1.masa * rapi1tg - part1.masa * rapi2tg + part2.masa * rapi2tg)/(part1.masa + part2.masa)
        part1.v = rapi1n * n + part1.rapi * tg 
        part2.v = rapi2n * n + part2.rapi * tg
        part1.posicion += part1.v * dt * 10
        part2.posicion += part2.v * dt * 10

def P(part):
    P = np.array([[0],
                  [1]]) * part.masa * g
    return P


def euler(part):
    sum_F = P(part)
    part.a = sum_F / part.masa
    part.v = part.v + part.a * dt
    

    
width = 600
height = 600
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
g = 9.8
dt = 0.0065
tiempos = []
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
timer_res = pygame.TIMER_RESOLUTION

n_part = 6
particulas = []

for i in range(0, n_part):
    radio_part = 30
    r_part = np.array([[random.uniform(radio_part, 600 - radio_part)],
                       [random.uniform(radio_part, 600 - radio_part)]])
    rapi_part = random.randint(0, 6)
    ang_part = random.uniform(0, 2 * np.pi)
    m_part = random.randint(1, 10)
    part = Particula(r_part, radio_part, rapi_part, ang_part, m_part)
    particulas.append(part)


#creo la matriz de rotacion de 90º en sentido horario
R = np.array([[0, -1],
              [1, 0]])


running = True
t = 0
pygame.init()
while running:
    screen.fill(white)
    for particula1 in particulas:
        lst_aux = list(particulas)
        lst_aux.remove(particula1)
        for particula2 in lst_aux:
            choque_elast(particula1, particula2)
        euler(particula1)
        particula1.moverse()
        particula1.dist_rec()
        particula1.rebotar()
        particula1.display()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()
    clock.tick(180)
    t += dt
