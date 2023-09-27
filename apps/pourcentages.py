def pourcentages():
    # Formule de bienvenue (pour la présentation)
    print("\n\n" + '{:━^61}'.format(" Calculons des pourcentages ! "))

    # Demande des valeurs
    nbq = int(input("Quelle est ta quantité ? "))   # Quantité
    nbtotal = int(input("Quel est ton total ? "))   # Total

    # Calcul et impression à l'écran
    print("Ton résultat est de " + str((nbq / nbtotal) * 100) + "%")

    # Formule de au revoir (pour la présentation)
    print('{:━^61}'.format(''))
