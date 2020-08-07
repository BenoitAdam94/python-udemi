from CardDeck import deck
import random

###########################
# distribution des cartes #
###########################

# Melanger le paquet

random.shuffle(deck)

# Initialisation des listes

player1deck = []
player2deck = []

# Distribution des cartes

for i in range(26):
    player1deck.append(deck[i])

for i in range(26,52):
    player2deck.append(deck[i])

# Affichage des jeux en liste (facultatif)

for i in range(26):
    print(player1deck[i])

print("")

for i in range(26):
    print(player2deck[i])

print("")

