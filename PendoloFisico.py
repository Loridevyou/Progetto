import pygame
import math

# Parametri del pendolo
l = float(input("Inserisci la lunghezza in pixel del filo: "))  # lunghezza del filo in pixel
G = 9.81  # accelerazione di gravità in m/s^2 (costante)
theta = math.pi / 4  # angolo iniziale (45 gradi)
omega = 0  # velocità angolare iniziale
r = float(input("Inserisci la lunghezza in pixel del raggio: "))  # raggio della sfera

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


# Funzione per aggiornare la posizione del pendolo
def posizione_pendolo(theta, omega, dt):
    alpha = -(G / l) * math.sin(theta)  # accelerazione angolare
    omega += alpha * dt  # aggiorna velocità angolare
    theta += omega * dt  # aggiorna angolo
    return theta, omega


# Tempo precedente
previous_time = pygame.time.get_ticks()

running = True #flag per gestione del ciclo while
count = 0 #inizializzo il contatore di oscillazioni
while running:
    # Calcola la posizione del pendolo
    x = b//2 + l * math.sin(theta)
    y = h//2 + l * math.cos(theta)

    # Calcola il tempo trascorso dall'ultimo frame in secondi
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - previous_time) / 1000.0  # converti in secondi dividendo i millisecondi
    previous_time = current_time #aggiorno il tempo di riferimento

    dt = delta_time  # tempo trascorso in secondi
    theta, omega = posizione_pendolo(theta, omega, dt)

    area.fill(black)
    pygame.draw.line(area, green, (b//2, h//2), (int(x), int(y)), 2)
    pygame.draw.circle(area, blue, (int(x), int(y)), r)
    pygame.display.flip()

    if theta == math.pi / 4:
        print(f"\nOscillazione: {count}")
        count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
