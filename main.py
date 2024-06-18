import os

def get_input(prompt: str, min_value: float, max_value: float):
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
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Valore deve essere tra {min_value} e {max_value}")
        except ValueError:
            print("Hai inserito un carattere non numerico")

def esegui_script(script_path):
    comando = f'python {script_path}'
    exit_status = os.system(comando)
    if exit_status == 0:
        print("Script eseguito correttamente.")
    else:
        print(f"Errore durante l'esecuzione dello script. Codice di uscita: {exit_status}")


scelta = get_input("Scegli se prendere i parametri dal file(1), o inserire da console(0)", 0, 1)
if scelta == 1:
    esegui_script('file.py')
elif scelta == 0:
    esegui_script('PendoloFisico.py')
else:
    print("Errore di inserimento")
