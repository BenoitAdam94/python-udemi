from CardDeck import deck
import random, time

player1deck = []
player2deck = []

# Distribution des cartes

for i in range(26):
    player1deck.append(deck[i])

for i in range(26,52):
    player2deck.append(deck[i])

# Affichage des jeux (facultatif)

for i in range(26):
    print(player1deck[i])

print("")

for i in range(26):
    print(player2deck[i])



