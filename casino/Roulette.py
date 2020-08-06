import math
import random


print ("Roulette Python")

# Mise de départ

jetons = 100

# boucle principale

while True:

    # affichage du nombre de jetons en court :

    print ("")
    print(f"Vous avez actuellement : {jetons} jetons")
    
    # Choisir un nombre entre 1 et 36

    
    while True :

        print("")
        nombre = input("Misez sur un nombre entre 1 et 36 : ")
        nombre = int(nombre)
        print("")

        if nombre >= 1 and nombre <= 36:
            break
        else:
            print("Nombre invalide !")

    while True:
        mise_nbre = input("Selectionner le nombre de jetons pour le nombre : ")
        mise_nbre = int(mise_nbre)

        mise_pair = input("Selectionner le nombre de jetons pour Pair : ")
        mise_pair = int(mise_pair)
        mise_impair = input("Selectionner le nombre de jetons pour Impair :")
        mise_impair = int(mise_impair)

        mise_manque = input("Selectionner le nombre de jetons pour Manque (1 a 18) : ")
        mise_manque = int(mise_manque)
        mise_passe = input("Selectionner le nombre de jetons pour Passe (19 a 36) : ")
        mise_passe = int(mise_passe)

        mise_rouge = input("Selectionner le nombre de jetons pour le rouge : ")
        mise_rouge = int(mise_rouge)
        mise_noir = input("Selectionner le nombre de jetons pour le noir : ")
        mise_noir = int(mise_noir)

        mise_total = mise_nbre + mise_rouge + mise_noir + mise_pair + mise_impair + mise_passe + mise_manque


        if nombre >= 1 and nombre <= 36 and mise_total > 0 and mise_total <= jetons:
            break
        else:
            print("")
            print("Mise non valide")
            print("")

    # recapitulatif de la mise totale :

    print(f"Vous avez misé un total de {mise_total} jetons")

    # Lancement de la bille et selection du numéro

    print ("")
    print ("Rien ne vas plus !")
    print ("")

    roulette = random.randint(0 , 36)

    # pour debuger (ou tricher à la roulette !)
    # roulette = 1

    print ("Et le numéro est :")
    print (roulette)

    # Initialisation du gain potentiel

    gain = 0

    # Si la bille vaut 0 tout va à la banque

    if roulette == 0 :
        print("tout pour la banque !")

    else :

        # pair & impair

        if (roulette % 2) == 0 :
            print("Pair")
            gain = gain + (mise_pair * 2)
        else:
            print("Impair")
            gain = gain + (mise_impair * 2)

        # 1-18 (Manque) | 19-26 (Passe)

        if roulette >= 1 and roulette <= 18 :
            print("Manque")
            gain = gain + (mise_manque * 2)
        else:
            print("Passe")
            gain = gain + (mise_passe * 2)

        # Couleur

        if roulette == (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
            print('Rouge')
            gain = gain + (mise_rouge * 2)
        else:
            print('Noir')
            gain = gain + (mise_noir * 2)
            
        # Nombre

        if nombre == roulette:
            print('Nombre exact ! Mise multipliée par 35 !!')
            gain = gain + (mise_nbre * 35)

    
    solde = gain - mise_total
    print(f"Vous avez gagné/perdu : {solde} jetons")
        
    jetons = jetons - mise_total + gain
    
    if jetons == 0:
        break

print("Vous n'avez plus de jetons ! Partie terminée !")