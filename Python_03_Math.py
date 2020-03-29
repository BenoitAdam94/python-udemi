import time #importe le module time
from time import sleep #importe importe uniquement ce que tu as besoin dans le module time
import math



print("Hello" + "World")
print("Python" * 3)

print (10 % 3) #modulo resultat = 1
print (10 // 3) #division entière resultat = 3
print (10 ** 3) #puissance résultat = 1000

print (" ")

print (math.ceil(-4.7)) # entier immédiatement supérieur, donne ici -4.
print (math.floor(-4.7)) # partie entière, donne ici -5.

print (math.exp(2)) # exponentielle.
print (math.factorial(5)) # factorielle 5, donc 120 ici (fonctionne uniquement pour les entiers positifs).

print (math.isinf(10/3)) # teste si x est infini (inf) et renvoie True si c'est le cas.
print (math.log(2)) # logarithme en base naturelle.
print (math.log(8, 2)) # log de 8 en base 2.
print (math.log10(2)) # logarithme en base 10.
print (math.pow(2, 3)) # 2 puissance 3 (peut aussi s'écrire 2 ** 3).
print (math.sqrt(16)) # racine carrée, donne ici 4.

print (math.degrees(1)) # convertit de radians en degrés.
print (math.radians(100)) # convertit de degrés en radians.

# Les constantes : #

print (math.pi) # (3.14159...)
print (math.e) # (2.71828...)