import pygame   #utilizzata per creare la finestra grafica e gestire il rendering.
import math

#la massa è la misura dell'inerzia di un corpo cioè la misura della resistenza che il corpo oppone alla variazione del suo stato di moto
m = float(input("Inserire la massa: "))
print(f"massa inserita = {m}kg")
#l'accelerazione è la variazione della velocità nel tempo, in questo caso l'accelerazione gravitazionale G
G = 9.81
# imposto una forza imprimibile a una certa massa
f = m*G
print(f"La forza risultante dalla prima legge della dinamica è = {f}")

#ora che sono presenti le variabili fisiche di base per qualsiasi corpo andiamo ad inserire le specifiche per il pendolo
#andremo, più avanti, ad inserire l'energia cinetica e potenziale
#nel pendolo fisico ideale, dove si idealizza una situazione senza attriti viscosi, la massa è ininfluente al moto del pendolo
l = float(input("Inserire lunghezza del filo: "))
print(f"lunghezza inserita = {l} metri")
#periodo
p = 2*math.pi*math.sqrt(l/G)

theta = float(input("Inserire l'ampiezza di partenza dell'angolo: "))
print(f"theta inserito = {theta}°")
#equazione del moto per l'accelerazione tangenziale
a = -G/l*math.sin(theta)


