import pygame
import math

pygame.init()

# Imposta la base e l'altezza della finestra
h = 600
b = 700

area = pygame.display.set_mode((b, h))

# Colori
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Parametri del pendolo
L = 250  # lunghezza del filo in pixel
g = 9.81  # accelerazione di gravità in m/s^2
theta = math.pi / 4  # angolo iniziale (45 gradi)
omega = 0  # velocità angolare iniziale

r = 15  # raggio della sfera
origin = (b // 2, h // 4)  # punto di fissaggio del pendolo

# Funzione per aggiornare la posizione del pendolo
def update_pendulum(theta, omega, dt):
    alpha = -(g / L) * math.sin(theta)  # accelerazione angolare
    omega += alpha * dt  # aggiorna velocità angolare
    theta += omega * dt  # aggiorna angolo
    return theta, omega

clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60) / 1000.0  # tempo trascorso in secondi
    theta, omega = update_pendulum(theta, omega, dt)

    # Calcola la posizione del pendolo
    x = origin[0] + L * math.sin(theta)
    y = origin[1] + L * math.cos(theta)

    area.fill(black)
    pygame.draw.line(area, green, origin, (int(x), int(y)), 2)
    pygame.draw.circle(area, blue, (int(x), int(y)), r)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
