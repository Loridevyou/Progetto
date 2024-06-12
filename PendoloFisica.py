import pygame   #utilizzata per creare la finestra grafica e gestire il rendering.
import math
import time     #libreria per gestione del tempo

pygame.init()   #serve per poter utilizzare pygame inizializzando i moduli

#imposto la base e l'altezza della finestra
h = 600 #altezza finestra
b = 700 #larghezza(base) finestra 

area = pygame.display.set_mode((b, h)) #creo la finestra

#il tipo di colore si basa sul formato RGB(red, green, blu)
red = (255, 0, 0)#scrivo 255 nella prima posizione per assegnare alla variabile red il colore rosso
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)#il nero è l'assenza di colore

r = 15 #raggio del cerchio

#creo punti di riferimento per le ascisse e le ordinate
vriga = h/2 # Posizione iniziale del pendolo rispetto all'asse verticale
origa = b/2 # Posizione iniziale del pendolo rispetto all'asse orizzontale

hgiro = vriga - 6*r #posizione centrale dell'orbita circolare (6*r è la lunghezza del filo)
#impostazione di tempo di pausa tra i frame
vel = 0.01 #(sarebbero i secondi in px al sec, quindi in questo caso è come dire: 1px/0.01sec = 100 px/1sec ->100px al secondo)

vrigaConst=vriga #conservo il valore iniziale di vriga
origaConst = origa #conservo il valore iniziale di di origa

count = 0
while count < 4:
    while vriga >= hgiro:
        pygame.draw.circle(area, blue, (origa, vriga), r) #luogo, colore, posizione estremo1(x, y), raggio
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro)) #luogo, colore, posizione estremo1(x, y), posizione estremo2
        pygame.display.update()#aggiorna la finestra
        time.sleep(vel)#questo metodo interrompe il programma per i secondi indicati
        area.fill(black)#imposto il colore del background della finestra
        vriga = vriga - 1 #il pendolo si sta muovendo verso l'alto lungo l'asse verticale della finestra, di 1px ogni ciclo
        origa = origaConst - math.sqrt((vrigaConst-hgiro)**2-(vriga-hgiro)**2)
        #sono necessarie le seguenti quattro righe di codice per poter semplicemente interrompere il programma
        events = pygame.event.get()#vengono prese tutte le azioni eseguite in input e memorizzate in questa lista
        for event in events:
            if event.type == pygame.QUIT:#se viene registrato un evento di chiusura forzata
                pygame.quit() #allora viene interrotto il programma
    origa1 = origa #conservo il valore iniziale di origa
    while vriga != vrigaConst:
        pygame.draw.circle(area, blue, (origa, vriga), r)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro))
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga + 1
        origa = origa1 + (origaConst - math.sqrt((vrigaConst-hgiro)**2-(vriga-hgiro)**2) - origa1)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    while vriga >= hgiro:
        pygame.draw.circle(area, blue, (origa, vriga), r)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro))
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga - 1
        origa = origaConst + math.sqrt((vrigaConst-hgiro)**2-(vriga-hgiro)**2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    origa2=origa
    while vriga != vrigaConst:
        pygame.draw.circle(area, blue, (origa, vriga), r)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro))
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga + 1
        origa = origa2 + (origaConst + math.sqrt((vrigaConst-hgiro)**2-(vriga-hgiro)**2) - origa2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    count = count + 1
    print(count)

