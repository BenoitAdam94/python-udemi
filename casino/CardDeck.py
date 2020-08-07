# from https://www.youtube.com/watch?v=kzJHgcp5MLo
import random

# list holders to place cards
cardfaces = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

# Start using loop to add content
for i in range (2,11):
    cardfaces.append(str(i))
    # this adds 2-10 and convert them to string data

for j in range (4):
    cardfaces.append(royals[j])
    #this will add the royal faces

# need to attach the suits to it

for k in range(4):
    for l in range(13):
        card = (cardfaces[l] + " of " + suits[k])
        deck.append(card)

# Verification du paquet
# for m in range(52):
#    print(deck[m])
# print("")

# Melange le paquet
random.shuffle(deck)

# impression du paquet
for m in range(52):
    print(deck[m])

print("")