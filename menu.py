# Cette variable ne sert qu'à la présentation du menu
bienvenue = "\n\n" + '{:━^61}'.format(' Bienvenue à toi !') +"\nTu es actuellement dans le menu de l'application !\nQue souhaites-tu faire ?"

# On initialise nos variables
user = 0

for loop in range(50):
    # On réinitialise nos variables
    user = 0

    print(bienvenue + "\n1 - Jouer au jeu de la bombe\n2 - Générer une présentation de toi\n3 - Trouver combien de fois un nombre est divisible par 2\n4 - Réviser tes tables de multiplication\n5 - Générer un tableau de conversion de monnaies\n6 - Calculons des pourcentages !\n9 - Quitter l'application")

    user = int(input("Rentre ici le numéro correspondant : "))
    if user == 1:
        from apps.jeu_bombe import *
    elif user == 2:
        from apps.age_calculator import *
    elif user == 3:
        from apps.nb_divisible_par_2 import *
    elif user == 4:
        from apps.reviseur_table_multi import *
    elif user == 5:
        from apps.money_convert import *
    elif user == 6:
        from apps.pourcentages import *


    elif user == 9:
        print("Merci d'avoir utilisé l'application !")