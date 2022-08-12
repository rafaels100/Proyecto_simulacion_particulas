import pygame

pygame.init()




size = (600, 600)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)


running = True



while running:
    screen.fill(white)
    pygame.draw.circle(screen, red, (300, 300), 30, 1)
    pygame.draw.line(screen, red, (0, 0), (300, 300), 1)
    print("asddsa")
    pygame.display.flip()
