# Istruzioni per l'uso del software

Questo software simula il movimento di un pendolo utilizzando la libreria `pygame` e calcola vari parametri fisici relativi al movimento del pendolo. Seguire le seguenti istruzioni è fondamentale per permettere all'utente l'utilizzo del programma, soddisfando tutte le richieste senza incorrere in eventuali bug.

## Requisiti
 Installa la libreria `pygame` eseguendo il comando:
   pip install pygame


# Utilizzo del software

## Passo 1: Importazione delle librerie
Il programma utilizza le librerie `pygame` e `math`.

## Passo 2: Parametri
Il programma richiede l'input di diversi parametri per configurare il pendolo.
I seguenti parametri possono essere presi dal file di testo "parametri.txt"(scegliendo 1),
oppure inseriti in input da console(scegliendo 2):

- **Lunghezza del filo (`l`)**: inserisci un valore in centimetri tra 1 e 10.
- **Massa della sfera (`massa`)**: inserisci un valore in chilogrammi tra 0.001 e 1.
- **Ampiezza angolare iniziale (`gradi_start`)**: inserisci un valore in gradi tra 1 e 90.
- **Coefficiente di attrito (`gamma`)**: inserisci un valore tra 0 e 1.

## Passo 3: Calcolo del raggio della sfera di ferro
Il raggio della sfera viene calcolato automaticamente in base alla massa inserita e alla densità del ferro(7870kg/m^3).

## Passo 4: Numero di Oscillazioni
- Se il coefficiente di attrito è zero, inserisci il numero di oscillazioni da visualizzare.
- Se è diverso da zero, il programma calcola automaticamente un numero di oscillazioni basato sull'attrito e sull'ampiezza iniziale.
(è possibile notare un continuo aumento del numero di oscillazioni nonostante il pendolo appaia come fermo, questo accade perchè il conteggio rileva anche spostamenti di pochi pixel e il conteggio procede fino a raggiungere il risultato dell'equazione per automatismo in caso di attrito)

## Passo 5: Esecuzione del Programma e possibili bug
Il programma visualizza una finestra dove viene mostrato il pendolo in movimento, insieme a vari dati relativi al movimento, come l'ampiezza angolare, la velocità angolare, il numero di oscillazioni, il periodo, l'energia potenziale e cinetica.
E' importante sapere che, in conseguenza di un piccolo malfunzionamento della libreria pygame con Visual studio, se l'utente sceglie di inserire i parametri da console, una volta inseriti tutti i dati si attiverà la finestra con la GUI di pygame ma è necessario cercare l'icona in basso ed aprirla "a mano" perchè viene overlayata dalla finestra della console di Visual studio. Se questa situazione dovesse generare un sentimento di fastidio da parte dell'utente o limitasse, in qualche modo, l'utilità del software nessun problema... le soluzioni sono due: è possibile eseguire lo script direttamente dalla console della bash di linux e visualizzare l'animazione senza limitazioni, oppure modificare il file di testo parametri.txt, inserendo i dati a propria scelta, e scegliere di eseguire lo script prendendo parametri da file (in questo caso non c'è interazione con la console e il problema non persiste).
Nel caso in cui si sceglie di inserire i parametri da file però l'utente deve stare attento ad inserire i dati nel file .txt nel modo corretto, principalmente: i valori dei dati devono essere inseriti nella stessa riga di dove sono richiesti e le righe non devono essere spostate, cancellate o modificate in alcun modo se non cambiando i valori.


## Esempio di inserimento 

lungezza filo(tra uno e dieci)cm: 10
massa sfera in kg: 0.5
angolo(tra zero e novanta)°: 80
attrito(tra zero e uno): 1
oscillazioni: 2

## Descrizione delle Funzioni

### Funzione: `posizione_pendolo`
Calcola la posizione, la velocità angolare, l'ampiezza e l'altezza del pendolo in ogni istante di tempo `dt`.

### Funzione: `get_input`
Prende un parametro in input e controlla se risulta valido secondo le regole impostate (valori minimi e massimi).

### Funzione: `calcola_raggio`
Calcola il raggio di una sfera data la sua massa e densità.

## Grafica
Il programma utilizza `pygame` per disegnare il pendolo e visualizzare i dati. La finestra ha una base di 1100 pixel e un'altezza di 700 pixel. La posizione del pendolo e i dati vengono aggiornati in tempo reale.

## Interruzione del Programma
Per interrompere il programma, chiudi la finestra `pygame` o attendi che il numero di oscillazioni specificato sia stato completato.
