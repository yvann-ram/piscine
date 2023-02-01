# Parti 1 : Simulation d’une luciole


# Constante SEUIL, qui détermine le seuil d’énergie au-delà duquel une luciole émet un flash.
SEUIL = 1.0
# Module ramdom pour générer des nombres aléatoires
import random as random

# --- Question 1 ----------------------------------------------------------------------------
# Fonction main. Dans lucioleEnergie j'ai initialisée aléatoirement entre 0. et 100. 
def main():
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)   
#print(main())


# --- Question 2 ----------------------------------------------------------------------------
# Fonction symboliseLuciole
def symboliseLuciole(niveauEnergie):
    if niveauEnergie >= SEUIL: # renvoie le caractère ’*’ si niveauEnergie est suffisant pour émettre un flash, et ’.’ sinon.
        return "*"
    else:
        return "."
#print(symboliseLuciole(1.0))


# --- Question 3 ----------------------------------------------------------------------------
# Fonction afficheLuciole
def afficheLuciole(niveauEnergie, verbeux):
    print(symboliseLuciole(niveauEnergie), end = "") # La fonction affiche le symbole de luciole correspondant à niveauEnergie.
    if verbeux == True: # Si verbeux est vrai, on affichera ensuite (sur la même ligne) le niveau d’énergie. 
        print(" ", niveauEnergie)
    print()
#print(afficheLuciole(1.0, True))


# --- Question 4 ----------------------------------------------------------------------------
# Modifier manuellement et plusieurs fois le niveau d’énergie de la luciole, et afficher la luciole après chaque modification.
#print(main(10))


# --- Question 5 ----------------------------------------------------------------------------
# Dans la fonction main.
def main():
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    # création d'une variable lucioleDeltaEnergie de type double, initialisation aléatoire entre 0. et 1.
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
#print(main())


# --- Question 6 ----------------------------------------------------------------------------
# Fonction incrementeLuciole qui prend en entrée deux nombres de type double appelés niveauEnergie et deltaEnergie, 
def incrementeLuciole(niveauEnergie, deltaEnergie):
    return niveauEnergie + deltaEnergie # renvoie le niveau d'énergie au pas de temps suivant
#print(incrementeLuciole(1.0, 1.0))


# --- Question 7 ----------------------------------------------------------------------------
# On utilise dans la fonction main la fonction définie précédemment pour faire évoluer le niveau d’énergie d’une luciole sur plusieurs pas de temps. 
# On conserve les affichages après chaque étape pour vérifier que l’affichage reste cohérent.
def main():
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
    for i in range(5):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        print("Energie de la luciole : ", lucioleEnergie)
#print(main())


# --- Question 8 ----------------------------------------------------------------------------
# fonction simuleLucioleNbPas qui initialise aléatoirement une luciole, et fait évoluer cette luciole un certain nombre de fois (fourni en paramètre), 
def simuleLucioleNbPas(nbPas):
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
    for i in range(nbPas):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        afficheLuciole(lucioleEnergie, True)
#print(simuleLucioleNbPas(5))


# --- Question 9 ----------------------------------------------------------------------------
# fonction simuleLucioleNbFlashs qui initialise aléatoirement une luciole, et qui affiche cette luciole en mode verbeux, 
def simuleLucioleNbFlashs(nbFlashs):
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
    for i in range(nbFlashs): # on tourne jusqu'à ce que le nombre de flashs soit atteint
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        afficheLuciole(lucioleEnergie, True)
        if lucioleEnergie >= SEUIL:
            print("Flash !")
#print(simuleLucioleNbFlashs(3))


# Léonardo Lopes
# E3IN 
# 2022-2023