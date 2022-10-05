# Formule de bienvenue (pour la présentation)
print("\n\n" + '{:━^61}'.format(' Et si on convertissait des monnaies ? '))

# On initialise les variables
dollar = 1.65   # Prix d'un dollar canadien en euros
euros = 1       # Euro actuel
n = 1           # Numéro d'affichage dans la liste

repeat = int(input("Combien de lignes souhaitez-vous générer (nombre entier strictement supérieur) ? "))

# On créé une boucle qui va répéter 8 fois notre programme
for loop in range(8):
    # On affiche une phrase qui nous permet d'afficher le résultat de la conversion
    print(str(n) + ". " + str(euros) + " euros = " + str(dollar * euros) + " $CAN")
    # On ajoute 1 au numéro d'affichage dans la liste puis on multiplie l'euro actuel par 2
    n += 1
    euros *= 2

# Formule de au revoir (pour la présentation)
print('{:━^61}'.format(''))