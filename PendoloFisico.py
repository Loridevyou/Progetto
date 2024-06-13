import pygame
import math

# Parametri del pendolo
l = float(input("Inserisci la lunghezza in centimetri del filo: ")) #lunghezza del filo in centimetri
l_cm = l*38 #ci sono, di media, circa 38 pixel ogni centimetro
G = 9.81  # accelerazione di gravità in m/s^2 (costante)
#gradi = float(input("Inserisci angolo inizale in gradi: ")) 
radianti = math.pi / 4  #angolo iniziale tra l'asse verticale e l'asse di riferimento del pendolo nell'istante iniziale -> 45 gradi
omega = 0  # velocità angolare iniziale
r = float(input("Inserisci la lunghezza in centimetri del raggio della sfera: "))  #raggio della sfera
r_cm = r*38 #conversione da pixel a centimetri

pygame.init()#serve per poter utilizzare pygame

# Imposta la base e l'altezza della finestra
h = 900 #altezza finestra
b = 1200 #larghezza(base) finestra

area = pygame.display.set_mode((b, h))#creo la finestra

#Il tipo di colore si basa sulla formattazione rgb(red, green, blu)
red = (255, 0, 0)#scrivo 255 nella prima posizione, ad esempio, per assegnare alla variabile red il colore rosso
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)#il nero è l'assenza di colore
#ho usato questi colori perchè erano i più semplici da impostare ma è possibile scegliere tra le varie combinazioni


# Funzione per aggiornare la posizione del pendolo in ogni istante, usando l'equazione di moto del pendolo semplice
def posizione_pendolo(radianti, omega, dt):
    alpha = -(G / l) * math.sin(radianti)  # accelerazione angolare -> variazione della velocità angolare nel tempo
    omega += alpha * dt  # velocità angolare all'istante dt -> variazione dell'ampiezza angolare nel tempo
    radianti += omega * dt  # ampiezza dell'angolo all'istante dt
    return radianti, omega

# Tempo iniziale
first_time = pygame.time.get_ticks()

run = True #flag per gestione del ciclo while
count = 0 #inizializzo il contatore di oscillazioni
while run:
    # Calcola la posizione del pendolo

    x = b//2 + l_cm * math.sin(radianti) #Posizione della sfera rispetto all'asse delle ascisse
    y = h//4 + l_cm * math.cos(radianti) #Posizione della sfera rispetto all'asse delle ordinate


    now = pygame.time.get_ticks() #Calcola il tempo trascorso dall'ultimo frame in secondi
    delta_time = (now - first_time) / 1000.0  # converti in secondi dividendo i millisecondi
    first_time = now #aggiorno il tempo di riferimento

    dt = delta_time  # tempo trascorso in secondi
    radianti, omega = posizione_pendolo(radianti, omega, dt)

    area.fill(black)
    pygame.draw.line(area, green, (b//2, h//4), (int(x), int(y)), 2)#luogo, colore, posizione estremo1(x, y), posizione estremo2

    pygame.draw.circle(area, blue, (int(x), int(y)), r)#luogo, colore, posizione estremo1(x, y), raggio

    pygame.draw.circle(area, blue, (int(x), int(y)), r_cm)#luogo, colore, posizione estremo1(x, y), raggio in cm

    pygame.display.update()#aggiorno lo schermo dopo le modifiche grafiche

    #Tengo il conto del numero di oscillazioni
    if radianti == math.pi / 4:
        print(f"\nOscillazione: {count}")
        count += 1 #incremento il contatore ogni volta che l'angolo torna ad essere 45°

    #Sono necessarie le seguenti quattro righe di codice per poter semplicemente interrompere il programma
    events = pygame.event.get()#vengono prese tutte le azioni eseguite in input e memorizzate in questa lista
    for event in events:
        if event.type == pygame.QUIT:#se viene registrato un evento di chiusura forzata
            run = False #allora viene interrotto il programma

pygame.quit()
