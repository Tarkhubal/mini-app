# Formule de bienvenue
print("\n\n" + '{:━^61}'.format(' Bienvenue Agent 008 ! '))

# Importation de bibliothèques
from random import *
from time import *

# Initialiser les variables
user_co = 0
essaie = 5

# Fonctions
def explode ():
    print("Vous n'avez pas trouvé la bombe !\nAttention ! La bombe va exploser !!")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1\nBOOM ! La bombe était placée en " + str(bombe) + " !")
    
# Choix de la difficulté
lvl_choice = int(input("Choisissons le niveau de difficulté de la partie !\nNiveau 1 : la bombe est cachée dans un interval de 21 nombres\nNiveau 2 : la bombe est cachée dans un interval de 11 nombres\nNiveau 3 : la bombe est cachée dans un interval de 5 nombres\nNiveau 4 : choissisez vous-même votre interval !\n\nEntrez votre niveau de difficulté (1, 2, 3 ou 4) ici : "))
if lvl_choice == 1:
    i = 10
elif lvl_choice == 2:
    i = 5
elif lvl_choice == 3:
    i = 2
elif lvl_choice == 4:
    i = int(input("Choisissez maintenant la taille de l'interval (nombre pair) : "))/2
else:
    print("\n\n\nMerci d'entrer un nombre entre 1 et 4.")

# Choix du nombre de joueurs
nb_joueur = int(input("Entrez le nombre de joueurs (1 ou 2): "))
while nb_joueur != 1 and nb_joueur != 2:
    nb_joueur = int(input("Merci d'entrer soit 1 soit 2 : "))

# Génération de la bombe
bombe = randint(0, 100)
print("Trouvez la bombe !")

# Fonction de debug
#print(bombe)

# Génération de l'interval de la bombe
l_co_bombe_min = bombe - i
l_co_bombe_max = bombe + i

# Mode solo
if nb_joueur == 1:
    while essaie == 5 or essaie == 4 or essaie == 3 or essaie == 2 or essaie == 1:
        user_co = int(input("Entrez un nombre entre 0 et 100 : "))
        if (user_co <= l_co_bombe_max and user_co >= l_co_bombe_min):
            print("Bravo ! Vous avez trouvé la bombe !")
            break
        elif user_co == bombe:
            print("Waouw quel sniper ! Vous avez trouvé l'emplacement exact de la bombe !")
            break
        else:
            print("Raté ! Il vous reste", str(essaie-1), "tentatives !")
            essaie -= 1

    if essaie == 0:
        explode()
    else:
        print("La bombe était placée en " + str(bombe) + " !")


# Mode deux joueurs
elif nb_joueur == 2:
    essaie_1 = 5
    essaie_2 = 5
    
    for loop in range(nb_joueur * 2):
        joueur_numero = 1
        print("\nJoueur " + str(joueur_numero) + ", prépare toi !\nC'est partiii !!")
        user_co = int(input("Entrez un nombre entre 0 et 100 : "))
        
        if (user_co <= l_co_bombe_max and user_co >= l_co_bombe_min):
            print("Bravo joueur " + str(joueur_numero) + "! Tu as trouvé la bombe !")
            break
        elif user_co == bombe:
            print("Waouw quel sniper " + str(joueur_numero) + " ! Vous avez trouvé l'emplacement exact de la bombe !")
            break
        else: 
            print("Raté joueur " + str(joueur_numero) + " ! Il te reste", str(essaie_1-1), "tentatives !")
            essaie_1 -= 1
        
        joueur_numero = 2
        print("\nJoueur " + str(joueur_numero) + ", prépare toi !\nOn y go !!")
        user_co = int(input("Entrez un nombre entre 0 et 100 : "))
        
        if (user_co <= l_co_bombe_max and user_co >= l_co_bombe_min):
            print("Bravo joueur " + str(joueur_numero) + "! Tu as trouvé la bombe !")
            break
        elif user_co == bombe:
            print("Waouw quel sniper " + str(joueur_numero) + " ! Vous avez trouvé l'emplacement exact de la bombe !")
            break
        else:
            print("Raté joueur " + str(joueur_numero) + " ! Il te reste", str(essaie_2-1), "tentatives !")
            essaie_2 -= 1
        
        
    
        # Si les deux joueurs n'ont pas trouvé :
        if essaie_1 == 0 or essaie_2 == 0:
            explode()
            break
    print("La bombe était placée en " + str(bombe) + " !")
        