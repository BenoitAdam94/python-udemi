import time #importe le module time
from time import sleep #importe importe uniquement ce que tu as besoin dans le module time


a = 0
b = 0

a = int(input("Entrez un nombre "))
b = int(input("Entrez un nombre "))

c = a + b
print(f"Le résultat de {a} + {b} est de {a+b}")

time.sleep(1)
sleep(1)
print("Compte a Rebours")

time.sleep(1)
print(c)
c = c-1

time.sleep(1)
print(c)
c = c-1

time.sleep(1)
print(c)
c = c-1

time.sleep(1)
print(c)
c = c-1