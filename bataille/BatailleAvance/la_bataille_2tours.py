from CardDeck import deck
from Distribution2or4Players import playerdeck
import random, time

# Bataille 2 tours (possibilité de sortir de la boucle infinie) 
# WIP

input("confirmer la distribution des cartes")

# fonction prendre une carte au hasard

# def tirer_une_carte(id_joueur):


while len(playerdeck[0]) != 0 and len(playerdeck[1]) != 0:

    random_card_j = []
    print("")

    # carte au hasard joueur 1

    random_card_j.append([random.choice(playerdeck[0])])
    playerdeck[0].remove(random_card_j[0][0])
    print(random_card_j[0][0])

    # carte au hasard joueur 2

    random_card_j.append([random.choice(playerdeck[1])])
    playerdeck[1].remove(random_card_j[1][0])
    print(random_card_j[1][0])



    # assignation d'une valeur au carte.

    j0_card = random_card_j[0][0][0]  # on prend le 1er caractere de la carte du j0

    if random_card_j[0][0][0] == '1': j0_card = 10
    if random_card_j[0][0][0] == 'J': j0_card = 11
    if random_card_j[0][0][0] == 'Q': j0_card = 12
    if random_card_j[0][0][0] == 'K': j0_card = 13
    if random_card_j[0][0][0] == 'A': j0_card = 14

    j0_card = int(j0_card) # transformation en int

    print(j0_card)

    j1_card = random_card_j[1][0][0]  # on prend le 1er caractere de la carte du j1

    if random_card_j[1][0][0] == '1': j1_card = 10
    if random_card_j[1][0][0] == 'J': j1_card = 11
    if random_card_j[1][0][0] == 'Q': j1_card = 12
    if random_card_j[1][0][0] == 'K': j1_card = 13
    if random_card_j[1][0][0] == 'A': j1_card = 14

    j1_card = int(j1_card) # transformation en int

    print(j1_card)
    print("")


    # comparaison des cartes et ajout des 2 carte au gagnant

    if j0_card > j1_card:
        print("joueur 1 gagne ce tour")
        playerdeck[0].append(random_card_j[0][0])
        playerdeck[0].append(random_card_j[1][0])
    elif j1_card > j0_card:
        print("joueur 2 gagne ce tour")
        playerdeck[1].append(random_card_j[0][0])
        playerdeck[1].append(random_card_j[1][0])
    elif j0_card == j1_card:
        print("Ex-Aquo")
        playerdeck[0].append(random_card_j[0][0])
        playerdeck[1].append(random_card_j[1][0])

    print(f"le joueur 1 a encore {len(playerdeck[0])} cartes")
    print(f"le joueur 2 a encore {len(playerdeck[1])} cartes")

    time.sleep(0.1)

if len(playerdeck[0]) != 0: print("Le joueur 1 a gagné !")
if len(playerdeck[1]) != 0: print("Le joueur 2 a gagné !")

