ville = "Ivry"
age = 33
nombre = 0
nombre = input("Entrez un nombre ")
print(nombre)

# Afficher le type d'une variable (fstring après Python 3.6)
print(f"la variable nombre est un {type(nombre)}")

# modification du type de variable via int : "int(nombre)"
nombre = int(nombre)

print(f"la variable nombre est un {type(nombre)}")
age = nombre + age


print(age)