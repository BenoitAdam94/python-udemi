from CardDeck import deck
import random

# Choix du nombre de joueurs

while True :

    print("")
    nombre_joueurs = input("Choisissez le nombre de joueurs (2 ou 4) ")
    nombre_joueurs = int(nombre_joueurs)
    print("")

    if nombre_joueurs == 2 or nombre_joueurs == 4:
        break
    else:
        print("Nombre invalide !")

print(nombre_joueurs)

# Initialisation des listes

range_nombre_joueurs = nombre_joueurs

playerdeck = []
for range_nombre_joueurs in range(range_nombre_joueurs) :
    playerdeck.append([])

print(playerdeck) # Doit imprimer le nombre de crochets correspondant au nombre de joueurs

# Definition du range selon le nombre de joueurs

nombre_carte = 52 // nombre_joueurs
print(nombre_carte)

# Distribution des cartes

for j in range(nombre_joueurs):
    for i in range(nombre_carte * j,nombre_carte+(nombre_carte * j)):
        playerdeck[j].append(deck[i])

# Impression des jeux

for j in range(nombre_joueurs):
    for i in range(nombre_carte):
        print(playerdeck[j][i])

    print("")


print("")