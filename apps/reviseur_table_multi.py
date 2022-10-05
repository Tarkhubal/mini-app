# Formule de bienvenue (pour la présentation)
print("\n\n" + '{:━^61}'.format(' Révisons nos tables de multiplication ! '))

# Importation de bibliothèques
from random import *

# On initialise les variables

# -- Configuration de l'application
nb_questions = 0    # Nombre de questions à poser
nb_min = 0          # Mutliplicateur minimum
nb_max = 0          # Multiplicateur maximum

# -- Application
score = 0           # Score de l'utilisateur
a = 0               # Nombre 1
b = 0               # Nombre 2
answer = 0          # Réponse de l'utilisateur
moyenne_score = 0   # Moyenne de l'utilisateur


# On demande à l'utilisateur de rentrer le nombre de questions à poser
nb_questions = int(input("Choisissez le nombre de questions : "))
print("Bien ! Choisissons maintenant quel interval de nombres vous voulez réviser.")
nb_min = int(input("Choisissez le nombre minimum : "))
nb_max = int(input("Choisissez le nombre maximum : "))

# On génère une boucle pour que le programme pose 10 questions
for loop in range(nb_questions):
    # On génère deux nombres aléatoires entre 1 et 10
    a = randint(nb_min, nb_max)
    b = randint(nb_min, nb_max)
    
    # On pose une question à l'utilisateur type "Combien font 3x5 ?" et on récupère sa réponse dans la variable "answer"
    answer = int(input("Combien font " + str(a) + "x" + str(b) + " ? "))
    
    # On détermine si le résultat qu'il a donné est bien égal au résultat du calcul
    if answer == a*b:
        # Si la réponse est correcte, on ajoute 1 au score
        score += 1
        print("Bravo ! Votre score est de " + str(score) + "/"+ str(nb_questions) + ".")
    else:
        print("Dommage ! La réponse était " + str(a*b) + ". Votre score est de " + str(score) + "/"+ str(nb_questions) + ".")

# On calcul la moyenne de l'utilisateur puis on l'affiche à l'écran
moyenne_score = (score/nb_questions)*20
print("Tu as une moyenne de " + str(round(moyenne_score, 2)) + "/20.")

# Et ici on affiche une phrase de félicitation ou de réprimande selon le score du joueur
if moyenne_score <= 0:
    print("Révise tes tables de multiplication !")
elif moyenne_score <= 8:
    print("Courage !! Tu peux encore t'améliorer !")
elif moyenne_score <= 10:
    print("Tu peux mieux faire !")
elif moyenne_score <= 16:
    print("Pas mal !")
else:
    print("Excellent !")

# Formule de au revoir (pour la présentation)
print("\n\n" + '{:━^61}'.format(''))