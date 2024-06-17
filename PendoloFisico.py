import pygame
import math

pygame.init()#serve per poter utilizzare pygame


# Funzione per aggiornare la posizione del pendolo in ogni istante(dt), usando l'equazione di moto del pendolo semplice
def posizione_pendolo(radianti: float, omega: float, dt: float) -> float:
    alpha = -(G / l) * math.sin(radianti) - gamma*omega  # accelerazione angolare -> variazione della velocità angolare nel tempo
    omega += alpha * dt  # velocità angolare all'istante dt -> variazione dell'ampiezza angolare nel tempo
    radianti += omega * dt  # ampiezza dell'angolo all'istante dt
    gradi = int(math.degrees(radianti)) # conversione da rad a gradi
    altezza = l*(1 - math.cos(radianti)) # altezza della sfera rispetto al punto più basso
    return radianti, omega, gradi, altezza
# Funzione per prendere in input valori float senza accettare caratteri o valori fuori dal range
def get_input(prompt: str, min_value: float, max_value: float) -> float:
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Valore deve essere tra {min_value} e {max_value}")
        except ValueError:
            print("Hai inserito un carattere non numerico")
# Funzione per prendere in input la massa e ritornare il raggio di una sfera, a seconda del materiale
def calcola_raggio(massa, densita):
    # Calcolo del volume dalla massa e dalla densità
    volume = massa / densita
    # Calcolo del raggio dalla formula del volume della sfera
    raggio_m = (3 * volume / (4 * math.pi)) ** (1/3)
    raggio_cm = raggio_m*100 #conversione da metri a cm
    return raggio_cm

# Parametri del pendolo
l = get_input("Inserisci la lunghezza in centimetri del filo (tra 1 e 10): ", 1, 10)  # lunghezza del filo in centimetri 
l_cm = l*38 #ci sono, di media, circa 38 pixel ogni centimetro

massa = get_input("Inserisci la massa della sfera (kg): ", 0.001, 100) #massa della sfera in kg

dens_ferro = 7870 #densità del ferro in kg/m^3

r = calcola_raggio(massa, dens_ferro)
r_cm = r*38 #ci sono, di media, circa 38 pixel ogni centimetro

G = 9.81  # accelerazione di gravità terrestre in m/s^2 (costante)
gradi_start = get_input("Inserisci l'ampiezza angolare iniziale in gradi (tra 1 e 90): ", 1, 90) #ampiezza iniziale(max 90)
radianti = math.radians(gradi_start)  # Conversione da gradi a radianti
omega = 0  # velocità angolare iniziale

gamma = get_input("Inserisci il coefficente di attrito(tra 0 e 1): ", 0, 1) #coefficente di attrito

if gamma == 0:
    #l'utente sceglie quante oscillazioni vedere prima di interrompere il programma
    while True:
        try:
            volonta = input("Inserisci quante oscillazioni vedere: ")  # lunghezza del filo in centimetri
            volonta = int(volonta)  # Prova a convertire l'input in un numero intero
            break
        except ValueError:
            print("Hai inserito un carattere non numerico")
else:
    volonta = 50 #se c'è attrito imposto di default 50 oscillazioni

I =  massa * l**2 #momento di inerzia del pendolo (considerando nulla la massa del filo)

# Imposta la base e l'altezza della finestra
h = 700 #altezza finestra
b = 1100 #larghezza(base) finestra
area = pygame.display.set_mode((b, h))#creo la finestra

#Il tipo di colore si basa sulla formattazione rgb(red, green, blu)
red = (255, 0, 0)#scrivo 255 nella prima posizione, ad esempio, per assegnare alla variabile red il colore rosso
green = (0, 255, 0) # Colore verde
blue = (0, 0, 255) # Colore blu
grey = (128, 128, 128)  # Colore grigio
black = (0, 0, 0)#il nero è l'assenza di colore
white = (255,255,255)#il bianco è la somma di tutti i colori
#ho usato questi colori perchè erano i più semplici da impostare ma è possibile scegliere tra le varie combinazioni(255^3)


#periodo -> tempo impiegato a compiere un oscillazione completa
periodo = round(2*math.pi*math.sqrt(l/G), 2)

#Inizio a generare delle stampe a schermo dei dati da visualizzare
#font e dimensione della scritta 
stile=pygame.font.Font('freesansbold.ttf',16)

# Tempo iniziale
first_time = pygame.time.get_ticks()

count = 0 #inizializzo il contatore di oscillazioni
last_direction = 1  # 1 per destra, -1 per sinistra

running = True

#interrompo il codice dopo 10 oscillazioni
while running:

    # Calcola la posizione del pendolo, considerando gli assi cartesiani
    x = b//2 + l_cm * math.sin(radianti) #Posizione della sfera rispetto all'asse delle ascisse
    y = h//4 + l_cm * math.cos(radianti) #Posizione della sfera rispetto all'asse delle ordinate


    now = pygame.time.get_ticks() #Calcola il tempo trascorso dall'ultimo frame in secondi
    dt = (now - first_time) / 1000.0  # converti in secondi dividendo i millisecondi
    first_time = now #aggiorno il tempo di riferimento

    radianti, omega, gradi, altezza = posizione_pendolo(radianti, omega, dt)
    En_pot = round(massa * G * altezza, 1) #m*g*h ,energia potenziale approssimata
    En_cin = round(1/2 * I * omega**2, 1) #I/2*omega**2 ,energia cinetica approssimata 


    #stamperà a schermo L'ampiezza iniziale
    outputAmax = "Ampiezza di partenza : " + str(gradi_start) + "°"
    testoAmax = stile.render(outputAmax, True, white)
    #genero una stringa che stamperà a schermo l'ampiezza del pendolo (la max è corrispondente a quella iniziale non essendoci attriti)
    outputA = "Ampiezza alpha: " + str(gradi) + "°"
    testoA=stile.render(outputA, True, white)
    #stamperà a schermo il valore assoluto della velocità angolare ad ogni istante
    o = math.copysign(omega, 1)#valore assoluto
    outputV = "Velocità angolare(val_abs): " + str(round(o, 1)) + "rad/sec"
    testoV=stile.render(outputV, True, white)
    #stamperà a schermo il numero di oscillazioni
    outputOs = "Numero oscillazioni: " + str(count)
    testoOs=stile.render(outputOs, True, white)
    #stampa a schermo il valore del periodo
    outputP = "Periodo(T): " + str(periodo) + "secondi"
    testoP=stile.render(outputP, True, white)
    #stampa a schermo l'energia potenziale
    outputEP = "Energia potenziale: " + str(En_pot) + " J"
    testoEP=stile.render(outputEP, True, white)
    #stampa a schermo l'energia cinetica
    outputEK = "Energia cinetica: " + str(En_cin) + " J"
    testoEK=stile.render(outputEK, True, white)

    #background
    area.fill(black)
    #linea di confronto
    pygame.draw.line(area, grey, (b//2, h//4), (b//2, h//4 + l_cm - r_cm))#asse delle ordinate
    #filo del pendolo
    pygame.draw.line(area, green, (b//2, h//4), (int(x), int(y)), 2)#luogo, colore, posizione estremo fisso, posizione estremo mobile
    #sfera
    pygame.draw.circle(area, blue, (int(x), int(y)), r_cm)#luogo, colore, posizione estremo1(x, y), raggio in cm
    
    #blitto il testo sullo schermo prima di aggiornarlo
    area.blit(testoAmax, (b/10, h/10 - 20))#blitto l'ampiezza max
    area.blit(testoA, (b/10, h/10))#blitto l'ampiezza aggiornata ad ogni istante
    area.blit(testoV, (b/10, h/10 + 20)) #sposto questa scritta di 20 pixel sotto l'altra
    area.blit(testoP, (b/10,h/10 + 40))#sposto questa scritta di 40 pixel sotto l'altra
    area.blit(testoOs, (b/1.5,h/10))#blitto le oscillazioni in alto a destra
    area.blit(testoEP, (b/1.5,h/10 + 20))#blitto energia potenziale in alto a destra
    area.blit(testoEK, (b/1.5,h/10 + 40))#blitto energia cinetica sotto quella potenziale
    
    pygame.display.update()#aggiorno lo schermo dopo le modifiche grafiche

    # Controlla se il pendolo ha attraversato la posizione iniziale (angolo zero) con cambio di direzione
    if last_direction > 0 and radianti < 0:
        if count > 0 and gamma != 0:
            periodo = (now - back)/1000 #calcolo periodo ogni oscillazione
        count += 1
        back = pygame.time.get_ticks()#aggiorno il tempo per calcolare il periodo
        print(f"\nOscillazione: {count}")

    # Aggiorna la direzione
    last_direction = 1 if radianti > 0 else -1
    

    #Sono necessarie le seguenti quattro righe di codice per poter semplicemente interrompere il programma
    events = pygame.event.get()#vengono prese tutte le azioni eseguite in input e memorizzate in questa lista
    for event in events:
        if event.type == pygame.QUIT:#se viene registrato un evento di chiusura forzata
            running = False
    #se il numero di oscillazioni viene superato si ferma il programma
    if count > volonta:
        running = False

pygame.quit() #usciti dal ciclo viene interrotto il programma


