# Formule de bienvenue (pour la présentation)
print("\n\n" + '{:━^61}'.format(" Calculons des pourcentages ! "))

# Demande des valeurs
nbq = int(input("Quelle est ta quantité ? "))
nbtotal = int(input("Quel est ton total ? "))

# Calcul et impression à l'écran
print("Ton résultat est de " + str((nbq / nbtotal) * 100) + "%")