import random

nombre_mystere = random.randint(0, 50)


i = 0
while i < 5 :
    nombre = input("Quel est le nombre mystère ? ")
    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        continue
    nombre = int(nombre)
    i = i + 1
    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()
print("Perdu !!!!!!!!!!")