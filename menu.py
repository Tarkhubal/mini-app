import os

from apps.age_calculator import age_calculator
from apps.jeu_bombe import jeu_bombes
from apps.nb_divisible_par_2 import nb_divisible_par_2
from apps.reviseur_table_multi import reviseur_table_multi
from apps.can_dollar import canadian_dollar
from apps.pourcentages import pourcentages

# Cette variable ne sert qu'à la présentation du menu
bienvenue = '{:━^61}'.format(' Bienvenue à toi !') +"\nTu es actuellement dans le menu de l'application !\nQue souhaites-tu faire ?"
os.system("cls")
while True:
    print(bienvenue + "\n1 - Jouer au jeu de la bombe\n" + \
        "2 - Générer une présentation de toi\n" + \
        "3 - Trouver combien de fois un nombre est divisible par 2\n" + \
        "4 - Réviser tes tables de multiplication\n" + \
        "5 - Générer un tableau de conversion de monnaies\n" + \
        "6 - Calculons des pourcentages !\n" + \
        "9 - Quitter l'application"
    )
    
    # On demande à l'utilisateur de choisir une option
    user = int(input("Rentre ici le numéro correspondant : "))
    
    os.system("cls")
    
    # Et on importe les apps en fontion de l'option choisie
    if user == 1:
        jeu_bombes()
    elif user == 2:
        age_calculator()
    elif user == 3:
        nb_divisible_par_2()
    elif user == 4:
        reviseur_table_multi()
    elif user == 5:
        canadian_dollar()
    elif user == 6:
        pourcentages()
    

    elif user == 9:
        print("Merci d'avoir utilisé l'application !")
    