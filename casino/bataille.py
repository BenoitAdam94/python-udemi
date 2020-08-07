from CardDeck import deck
import random, time

player1deck = []
player2deck = []

for i in range(26):
    player1deck.append(deck[i])

for i in range(26,52):
    player2deck.append(deck[i])

# Impression des jeux

for i in range(26):
    print(player1deck[i])

print("")

for i in range(26):
    print(player2deck[i])



