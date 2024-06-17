import tkinter as tk
import math

# Funzione per prendere in input la massa e ritornare il raggio di una sfera, a seconda del materiale
def calcola_raggio(massa, densita):
    # Calcolo del volume dalla massa e dalla densità
    volume = massa / densita
    # Calcolo del raggio dalla formula del volume della sfera
    raggio_m = (3 * volume / (4 * math.pi)) ** (1 / 3)
    raggio_cm = raggio_m * 100  # conversione da metri a cm
    return raggio_cm

def get_input():
    l = float(entry_l.get())
    massa = float(entry_massa.get())
    gradi_start = float(entry_gradi.get())
    gamma = float(entry_gamma.get())

    if l < 1 or l > 10:
        label_error.config(text="La lunghezza deve essere tra 1 e 10 cm")
        return
    if massa < 0.001 or massa > 10:
        label_error.config(text="La massa deve essere tra 0.001 e 10 kg")
        return
    if gradi_start < 1 or gradi_start > 90:
        label_error.config(text="L'ampiezza angolare deve essere tra 1 e 90 gradi")
        return
    if gamma < 0 or gamma > 1:
        label_error.config(text="Il coefficiente di attrito deve essere tra 0 e 1")
        return

    label_error.config(text="")

    l_cm = l * 38
    dens_ferro = 7870
    r = calcola_raggio(massa, dens_ferro)
    r_cm = r * 38
    print(f"La sfera di ferro con massa {massa}kg ha raggio {round(r, 3)}cm")

    G = 9.81
    radianti = math.radians(gradi_start)
    omega = 0

    if gamma == 0:
        while True:
            try:
                volonta = int(entry_oscillazioni.get())
                break
            except ValueError:
                label_error.config(text="Inserisci un numero intero per le oscillazioni")
                return
    else:
        volonta = 50

    # Qui puoi eseguire il codice per la simulazione del pendolo utilizzando i valori inseriti

root = tk.Tk()
root.title("Simulazione Pendolo")

label_l = tk.Label(root, text="Lunghezza del filo (cm):")
label_l.grid(row=0, column=0)
entry_l = tk.Entry(root)
entry_l.grid(row=0, column=1)

label_massa = tk.Label(root, text="Massa della sfera (kg):")
label_massa.grid(row=1, column=0)
entry_massa = tk.Entry(root)
entry_massa.grid(row=1, column=1)

label_gradi = tk.Label(root, text="Ampiezza angolare iniziale (gradi):")
label_gradi.grid(row=2, column=0)
entry_gradi = tk.Entry(root)
entry_gradi.grid(row=2, column=1)

label_gamma = tk.Label(root, text="Coefficiente di attrito:")
label_gamma.grid(row=3, column=0)
entry_gamma = tk.Entry(root)
entry_gamma.grid(row=3, column=1)

label_oscillazioni = tk.Label(root, text="Numero di oscillazioni (se attrito = 0):")
label_oscillazioni.grid(row=4, column=0)
entry_oscillazioni = tk.Entry(root)
entry_oscillazioni.grid(row=4, column=1)

button_submit = tk.Button(root, text="Avvia simulazione", command=get_input)
button_submit.grid(row=5, column=0, columnspan=2)

label_error = tk.Label(root, text="", fg="red")
label_error.grid(row=6, column=0, columnspan=2)

root.mainloop()