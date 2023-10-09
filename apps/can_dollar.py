def canadian_dollar():
    # Formule de bienvenue (pour la présentation)
    print('{:━^61}'.format(' Et si on convertissait des monnaies ? '))

    # On initialise les variables
    dollar = 1.65   # Prix d'un dollar canadien en euros
    euros = 1       # Euro actuel

    repeat = int(input("Combien de lignes souhaitez-vous générer (nombre entier strictement supérieur) ? "))

    # On créé une boucle qui va répéter 8 fois notre programme
    for i in range(repeat):
        # On affiche une phrase qui nous permet d'afficher le résultat de la conversion
        print(f"{i+1}. {euros} euros = {dollar * euros} $CAN")
        # On ajoute 1 au numéro d'affichage dans la liste puis on multiplie l'euro actuel par 2
        euros *= 2

    # Formule de au revoir (pour la présentation)
    print('{:━^61}'.format(''))
