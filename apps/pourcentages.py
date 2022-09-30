play = 0
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Bienvenue sur l'application pourcentages !")

while play != 1:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\nQuelle est ta quantité ?")
    nb1 = int(input())

    print("Quel est ton total?")
    nbtotal = int(input())

    print("Ton résultat est de ", end="")
    print((nb1 / nbtotal) * 100, end="")
    print("%")

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    print(
        "Pour stopper le programme, entrez [0], si vous souhaitez continuer sur cette application, entrez [1]"
    )
    c = int(input())
    if c == 0:
        play = 1

play = 0