from CardDeck import deck
from card_distribution2players import player1deck, player2deck
import random, time

# Bataille simple
# Boucle infinie sauf si l'un des joueurs a les 4 as au début de la partie

input("confirmer la distribution des cartes")

while len(player1deck) != 0 and len(player2deck) != 0:

    print("")
    # carte au hasard joueur 1

    random_card_j1 = random.choice(player1deck)
    player1deck.remove(random_card_j1)
    print(random_card_j1)

    # carte au hasard joueur 2

    random_card_j2 = random.choice(player2deck)
    player2deck.remove(random_card_j2)
    print(random_card_j2)

    # assignation d'une valeur au carte.

    j1_card = random_card_j1[0]  # on prend le 1er caractere de la carte du j1

    if random_card_j1[0] == '1': j1_card = 10
    if random_card_j1[0] == 'J': j1_card = 11
    if random_card_j1[0] == 'Q': j1_card = 12
    if random_card_j1[0] == 'K': j1_card = 13
    if random_card_j1[0] == 'A': j1_card = 14

    j1_card = int(j1_card) # transformation en int

    j2_card = random_card_j2[0]  # on prend le 1er caractere de la carte du j2

    if random_card_j2[0] == '1': j2_card = 10
    if random_card_j2[0] == 'J': j2_card = 11
    if random_card_j2[0] == 'Q': j2_card = 12
    if random_card_j2[0] == 'K': j2_card = 13
    if random_card_j2[0] == 'A': j2_card = 14

    j2_card = int(j2_card) # transformation en int

    print("")

    # comparaison des cartes et ajout des 2 carte au gagnant

    if j1_card > j2_card:
        print("joueur 1 gagne ce tour")
        player1deck.append(random_card_j1)
        player1deck.append(random_card_j2)
    elif j2_card > j1_card:
        print("joueur 2 gagne ce tour")
        player2deck.append(random_card_j1)
        player2deck.append(random_card_j2)
    elif j1_card == j2_card:
        print("Ex-Aquo")
        player1deck.append(random_card_j1)
        player2deck.append(random_card_j2)

    # Affichage du nombre de cartes restant

    print(f"le joueur 1 a encore {len(player1deck)} cartes")
    print(f"le joueur 2 a encore {len(player2deck)} cartes")

    time.sleep(0.1)

if len(player1deck) != 0: print("Le joueur 1 a gagné !")
if len(player2deck) != 0: print("Le joueur 2 a gagné !")