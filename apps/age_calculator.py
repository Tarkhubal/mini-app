def age_calculator():
    # Formule de bienvenue (pour la présentation)
    print("\n\n" + '{:━^61}'.format(' Générons une présentation de toi ! '))

    # On initialise les variables
    prenom = nom = annee_naissance = age = 0

    # On demande à l'utilisateur de rentrer son prénom, son nom et sa date de naissance
    prenom = input("Quel est votre prénom ? ")
    nom = input("Quel est votre nom ? ")
    annee_naissance = int(input("Quel est votre année de naissance ? "))

    # On calcule l'âge de l'utilisateur
    age = 2022 - annee_naissance

    print(f"Bonjour {prenom} {nom}, vous avez {age} an{'s' if age > 1 else ''}.")

    # Formule de au revoir (pour la présentation)
    print('{:━^61}'.format(''))
