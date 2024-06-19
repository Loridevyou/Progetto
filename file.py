import pygame
import math
import re

pygame.init()#serve per poter utilizzare pygame

def posizione_pendolo(radianti: float, omega: float, dt: float) -> tuple:
    """
    Funzione: posizione_pendolo
    Calcola la posizione, la velocità angolare, l'ampiezza e l'altezza del pendolo.
    Parametri formali:
    radianti (float): Angolo in radianti.
    omega (float): Velocità angolare in radianti.
    dt (float): Intervallo di tempo in secondi.
    Valore di ritorno:
    (radianti, omega, gradi, altezza)
    """
    alpha = -(G / l) * math.sin(radianti) - gamma * omega
    omega += alpha * dt
    radianti += omega * dt
    gradi = int(math.degrees(radianti))
    altezza = l * (1 - math.cos(radianti))
    return radianti, omega, gradi, altezza

def calcola_raggio(massa, densita):
    """
    Funzione: calcola_raggio
    Calcola il raggio di una sfera data la sua massa e densità.
    Parametri formali:
    massa (float): La massa della sfera in kg.
    densita (float): La densità della sfera in kg/m^3.
    Valore di ritorno:
    float: Il raggio della sfera in centimetri.
    """
    volume = massa / densita
    raggio_m = (3 * volume / (4 * math.pi)) ** (1/3)
    raggio_cm = raggio_m * 100
    return raggio_cm

def get_input_mod(n: str, min_value: float, max_value: float):
    """
    Funzione: get_input
    Prende un parametro in input e controlla se risulta valido secondo le regole impostate.
    Parametri formali:
        prompt (str): Testo in output.
        min_value (float): Valore minimo nel range della validità.
        max_value (float): Valore massimo nel range della validità.
    Valore di ritorno:
        value
    """
    value = n
    if min_value <= value <= max_value:
        return value
    else:
        print(f"Valore deve essere tra {min_value} e {max_value}")
        return None

def leggi_numero(riga):
    """
    Funzione: leggi_numero
    Estrae un numero float da una riga di testo.
    Parametri formali:
        riga: Una stringa che rappresenta la riga di testo.
    Valore di ritorno:
        Il numero float estratto dalla riga, oppure None se non viene trovato un numero.
    """
    # Espressione regolare per un numero float
    numero_regex = r"\d+(\.\d+)?" #? significa che l'elemento precedente è opzionale, \d+ significa che c'è un numero decimale con una o più cifre, il \. corrisponde a un punto letterale.
    match = re.search(numero_regex, riga) #metodo regex per cercare l'elemento, dato dall'espressione regolare, in ogni riga
    if match:
        return float(match.group(0)) #se l'elemento corrisponde ai parametri dell'espressione
    else:
        return None #se l'elemento non corrisponde

# Lettura dei parametri dal file di testo, utilizzo il with-as per isolare questa parte di codice
with open("parametri.txt", "r") as file:
    linee = file.readlines()

    l = get_input_mod(leggi_numero(linee[0]), 1, 10) # Lunghezza del filo in cm
    if l is None:
        raise ValueError("Valore lunghezza filo non valido") #mando messaggio d'errore e non faccio partire il programma per evitare il bug
    
    l_cm = l * 38

    massa = get_input_mod(leggi_numero(linee[1]), 0.1, 50)  # Massa della sfera in kg
    if massa is None:
        raise ValueError("Valore massa sfera non valido")
    dens_ferro = 7870  # densità del ferro in kg/m^3
    r = calcola_raggio(massa, dens_ferro)
    r_cm = r * 38
    print(f"La sfera di ferro con massa {massa}kg ha raggio {round(r, 3)}cm")
    G = 9.81  # accelerazione di gravità terrestre in m/s^2 (costante)

    gradi_start = get_input_mod(leggi_numero(linee[2]), 1, 90)  # ampiezza angolare iniziale in gradi
    if gradi_start is None:
        raise ValueError("Valore gradi non valido")
    
    radianti = math.radians(gradi_start)
    omega = 0  # velocità angolare iniziale

    gamma = get_input_mod(leggi_numero(linee[3]), 0, 1)  # coefficente di attrito
    if gamma is None:
        raise ValueError("Valore attrito non valido")

    #se c'è attrito imposto questa equazione (risultato di varie sperimentazioni), il programma termina circa quando il pendolo si ferma
    volonta = (1 - gamma)*10 + int(gradi_start/10)-1 if gamma == 0 else get_input_mod(leggi_numero(linee[4]), 1, 100)
    if volonta is None:
        raise ValueError("Valore numero di oscillazioni non valido")
    

# momento di inerzia del pendolo (considerando nulla la massa del filo)
I = massa * l**2 


#periodo -> tempo impiegato a compiere un oscillazione completa
periodo = round(2*math.pi*math.sqrt(l/G), 2)

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

#Inizio a generare delle stampe a schermo dei dati da visualizzare
#font e dimensione della scritta 
stile=pygame.font.Font('freesansbold.ttf',16)

# Tempo iniziale
first_time = pygame.time.get_ticks()

count = 0 #inizializzo il contatore di oscillazioni
last_direction = 1  # 1 per destra, -1 per sinistra

running = True

#partenza del ciclo while
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


