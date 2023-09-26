# On demande à l'utilisateur de rentrer un nombre entier strictement positif
n = int(input("Entre un entier strictement positif : "))

while n < 1:
    n = int(input("Entre un entier STRICTEMENT POSITIF s'il te plait : "))

# On initialise les variables et on sauvegarde le nombre de départ
nbdonne_save = n
comptage = 0

# On divise n par 2 et on ajoute 1 à un compteur jusqu'à ce que le nombre soit égal à 0 ou 1 (donc qu'il n'est plus
# divisible par 2)

while n%2 == 0:
    n /= 2
    comptage += 1

# On affiche le résultat avec une belle phrase
if comptage == 0:
    print(str(nbdonne_save) + " n'est pas divisible par 2.")
else:
    print(str(nbdonne_save) + " est " + str(comptage) + " fois divisible par 2.")