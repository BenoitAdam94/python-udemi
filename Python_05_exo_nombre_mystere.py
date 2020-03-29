import time #importe le module time
from time import sleep #importe importe uniquement ce que tu as besoin dans le module time
import math


i = 7

print ("Quel est le nombre mystere ?")

nombre = input("Entrez un nombre ")
nombre = int(nombre)

if nombre == i:
    print("bravo")
    
elif nombre > i:
    print(f"Le nombre mystère est plus petit que {nombre}")
    
else:
    print("c'est plus")