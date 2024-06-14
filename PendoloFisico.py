import pygame
import math

pygame.init()#serve per poter utilizzare pygame

# Parametri del pendolo
while True:
    l = float(input("Inserisci la lunghezza in centimetri del filo (tra 1 e 10): ")) #lunghezza del filo in centimetri
    if l>10 or l<1:
        print("Valore massimo 10, valore minimo 1")
    else:
        break
l_cm = l*38 #ci sono, di media, circa 38 pixel ogni centimetro

while True:
    r = float(input("Inserisci la lunghezza in centimetri del raggio della sfera(tra 0.1 e 2): "))  #raggio della sfera
    if r>2 or r<0.1:
        print("Valore massimo 2, valore minimo 0.1")
    else:
        break
r_cm = r*38 #conversione da pixel a centimetri

G = 9.81  # accelerazione di gravità in m/s^2 (costante)
radianti = math.pi / 4  #angolo iniziale tra l'asse verticale e l'asse di riferimento del pendolo nell'istante iniziale -> 45 gradi
gradi_start = int(radianti*57.2958) #conversione da rad a gradi
omega = 0  # velocità angolare iniziale

# Imposta la base e l'altezza della finestra
h = 700 #altezza finestra
b = 1100 #larghezza(base) finestra
area = pygame.display.set_mode((b, h))#creo la finestra

#Il tipo di colore si basa sulla formattazione rgb(red, green, blu)
red = (255, 0, 0)#scrivo 255 nella prima posizione, ad esempio, per assegnare alla variabile red il colore rosso
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)  # Colore grigio
black = (0, 0, 0)#il nero è l'assenza di colore
white = (255,255,255)#il bianco è la somma di tutti i colori
#ho usato questi colori perchè erano i più semplici da impostare ma è possibile scegliere tra le varie combinazioni


# Funzione per aggiornare la posizione del pendolo in ogni istante, usando l'equazione di moto del pendolo semplice
def posizione_pendolo(radianti, omega, dt):
    alpha = -(G / l) * math.sin(radianti)  # accelerazione angolare -> variazione della velocità angolare nel tempo
    omega += alpha * dt  # velocità angolare all'istante dt -> variazione dell'ampiezza angolare nel tempo
    radianti += omega * dt  # ampiezza dell'angolo all'istante dt
    gradi = int(radianti*57.2958) #conversione da rad a gradi
    return radianti, omega, gradi


#Inizio a generare delle stampe a schermo dei dati da visualizzare
#font e dimensione della scritta 
stile=pygame.font.Font('freesansbold.ttf',16)

# Tempo iniziale
first_time = pygame.time.get_ticks()

count = 0 #inizializzo il contatore di oscillazioni
last_direction = 1  # 1 per destra, -1 per sinistra

#interrompo il codice dopo 8 oscillazioni
while count <= 8:

    # Calcola la posizione del pendolo

    x = b//2 + l_cm * math.sin(radianti) #Posizione della sfera rispetto all'asse delle ascisse
    y = h//4 + l_cm * math.cos(radianti) #Posizione della sfera rispetto all'asse delle ordinate


    now = pygame.time.get_ticks() #Calcola il tempo trascorso dall'ultimo frame in secondi
    delta_time = (now - first_time) / 1000.0  # converti in secondi dividendo i millisecondi
    first_time = now #aggiorno il tempo di riferimento

    dt = delta_time  # tempo trascorso in secondi
    radianti, omega, gradi = posizione_pendolo(radianti, omega, dt)
    
    #stamperà a schermo L'ampiezza iniziale
    outputAmax = "Ampiezza di partenza : " + str(gradi_start) + "°"
    testoAmax=stile.render(outputAmax, True, white)
    #genero una stringa che stamperà a schermo l'ampiezza del pendolo (la max è corrispondente a quella iniziale non essendoci attriti)
    outputA = "Ampiezza : " + str(gradi) + "°"
    testoA=stile.render(outputA, True, white)
    #stamperà a schermo la velocità angolare ad ogni istante
    outputV = "Velocità angolare: " + str(round(omega, 1)) + "rad/sec"
    testoV=stile.render(outputV, True, white)
    #stamperà a schermo il numero di oscillazioni
    outputOs = "Numero oscillazioni: " + str(count)
    testoOs=stile.render(outputOs, True, white)

    area.fill(black)
    pygame.draw.line(area, grey, (b//2, h//4), (b//2, h//4 + l_cm - r_cm))#asse delle ordinate
    pygame.draw.line(area, green, (b//2, h//4), (int(x), int(y)), 2)#luogo, colore, posizione estremo fisso, posizione estremo mobile

    pygame.draw.circle(area, blue, (int(x), int(y)), r)#luogo, colore, posizione estremo1(x, y), raggio

    pygame.draw.circle(area, blue, (int(x), int(y)), r_cm)#luogo, colore, posizione estremo1(x, y), raggio in cm
    
    #blitto il testo sullo schermo prima di aggiornarlo
    area.blit(testoAmax, (b/10, h/10 - 20))#blitto l'ampiezza max
    area.blit(testoA, (b/10, h/10))#blitto l'ampiezza aggiornata ad ogni istante
    area.blit(testoV, (b/10, h/10 + 20)) #sposto questa scritta di 15 pixel sotto l'altra
    area.blit(testoOs, (b/1.5,h/10))#blitto le oscillazioni in alto a destra
    
    pygame.display.update()#aggiorno lo schermo dopo le modifiche grafiche

    # Controlla se il pendolo ha attraversato la posizione iniziale (angolo zero) con cambio di direzione
    if last_direction > 0 and radianti < 0:
        count += 1
        print(f"\nOscillazione: {count}")
    elif last_direction < 0 and radianti > 0:
        count += 1
        print(f"\nOscillazione: {count}")

    # Aggiorna la direzione
    last_direction = 1 if radianti > 0 else -1
    

    #Sono necessarie le seguenti quattro righe di codice per poter semplicemente interrompere il programma
    events = pygame.event.get()#vengono prese tutte le azioni eseguite in input e memorizzate in questa lista
    for event in events:
        if event.type == pygame.QUIT:#se viene registrato un evento di chiusura forzata
            pygame.quit() #allora viene interrotto il programma


