# Formule de bienvenue (pour la présentation)
print("\n\n" + '{:━^61}'.format(' Révisons nos tables de multiplication ! '))

# Importation de bibliothèques
from random import *

# Initialisation des variables
score = 0   # Score du joueur
a = 0       # Nombre 1
b = 0       # Nombre 2

# On génère une boucle pour que le programme pose 10 questions
for loop in range(10):
    # On génère deux nombres aléatoires entre 1 et 10
    a = randint(1, 10)
    b = randint(1, 10)
    
    # On pose une question à l'utilisateur type "Quel est le résultat de 3x5 ?"
    print("Quel est le résultat de " + str(a) + "x" + str(b) + " ?")
    
    # On demande à l'utilisateur de rentrer une réponse puis on détermine si il est égal au résultat du calcul
    if int(input()) == a*b:
        # Si la réponse est correcte, on ajoute 1 au score
        score += 1
        print("Bravo ! Votre score est maintenant de " + str(score) + ".")
    else:
        # Si la réponse est fausse, on soustrait 1 au score
        score -= 1
        print("Dommage ! La réponse était " + str(a*b) + ". Votre score est maintenant de " + str(score) + ".")
    print("\n\nQuestion suivante !!\n")

# Et ici on affiche une phrase de félicitation ou de réprimande selon le score du joueur
if score == 0:
    print("Révise tes tables de multiplication !")
elif score <= 5:
    print("Tu peux mieux faire !")
elif score <= 8:
    print("Pas mal !")
else:
    print("Excellent !")