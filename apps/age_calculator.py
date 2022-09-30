print("\n\n" + '{:━^61}'.format(' Générons une présentation de toi ! '))

prenom = input("Quel est votre prénom ? ")
nom = input("Quel est votre nom ? ")
annee_naissance = int(input("Quel est votre année de naissance ? "))

age = 2022 - annee_naissance

print("Bonjour " + prenom + " " + nom + ", vous avez " + str(age) + " ans.")
print('{:━^61}'.format(''))