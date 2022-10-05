# Formule de bienvenue (pour la présentation)
print("\n\n" + '{:━^61}'.format(' Générons une présentation de toi ! '))

# On initialise les variables
prenom = 0          # Prénom de l'utilisateur
nom = 0             # Nom de l'utilisateur
annee_naissance = 0 # Année de naissance de l'utilisateur
age = 0             # Age de l'utilisateur

# On demande à l'utilisateur de rentrer son prénom, son nom et sa date de naissance
prenom = input("Quel est votre prénom ? ")
nom = input("Quel est votre nom ? ")
annee_naissance = int(input("Quel est votre année de naissance ? "))

# On calcule l'âge de l'utilisateur
age = 2022 - annee_naissance

# On affiche une phrase type "Bonjour Thomas BLANC, vous avez 16 ans."
print("Bonjour " + prenom + " " + nom + ", vous avez " + str(age) + " ans.")

# Formule de au revoir (pour la présentation)
print('{:━^61}'.format(''))