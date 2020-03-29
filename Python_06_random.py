import random

a = random.randint(0, 50)
b = random.randint(0, 50)
c = random.randrange(2) # 0 et 1 (2 exclu)
c = random.randrange(0, 101, 10) # tous les 10
e = random.uniform(0, 1) # float entre 0 et 1

if a > b:
    print("Le nombre a est plus grand que le nombre b.")
elif b > a:
    print("Le nombre b est plus grand que le nombre a.")
else:
    print("Le nombre a et le nombre b sont égaux")
