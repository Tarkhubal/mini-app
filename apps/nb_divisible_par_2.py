n = int(input("Entrez un entier strictement positif : "))

while n<1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF :"))

nbdonne_save = n
comptage = 0

while n%2 == 0:
    n /= 2
    comptage += 1

print(str(nbdonne_save) + " est " + str(comptage) + " fois divisible par 2.")