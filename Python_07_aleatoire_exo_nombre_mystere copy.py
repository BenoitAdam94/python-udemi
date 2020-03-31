import math
import random


i = random.randint(0 , 50)

print ("Quel est le nombre mystere ?")

nombre = input("Entrez un nombre ")
nombre = int(nombre)

if nombre == i:
    print("bravo")
    
elif nombre > i:
    print(f"Le nombre mystère est plus petit que {nombre}")
    
else:
    print("c'est plus")