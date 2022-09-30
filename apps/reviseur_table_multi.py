# Formule de bienvenue
print("\n\n" + '{:━^61}'.format(' Révisons nos tables de multiplication ! '))

# Importation de bibliothèques
from random import *

# Initialisation des variables
score = 0

for loop in range(10):
    a = randint(1, 10)
    b = randint(1, 10)
    
    print("Quel est le résultat de " + str(a) + "x" + str(b) + " ?")
    if int(input()) == a*b:
        score += 1
        print("Bravo ! Votre score est maintenant de " + str(score) + ".")
    else:
        score -= 1
        print("Dommage ! La réponse était " + str(a*b) + ". Votre score est maintenant de " + str(score) + ".")
    print("\n\nQuestion suivante !!\n")
    
if score == 0:
    print("Révise tes tables de multiplication !")
elif score <= 5:
    print("Tu peux mieux faire !")
elif score <= 8:
    print("Pas mal !")
else:
    print("Excellent !")