# Importation de bibliothèques
from random import *

# On initialise les variables

# -- Variables communes au deux modes de jeu (par ordre d'apparition) :
i = 0               # Interval de la position de la bombe
nb_joueur = 0       # Choix du nombre de joueurs

bombe = 0           # Coordonnées de la bombe
l_co_bombe_min = 0  # Coordonnées minimales de la bombe
l_co_bombe_max = 0  # Coordonnées maximales de la bombe
user_co = 0         # Coordonnée donnée par l'utilisateur

# -- Mode 1 joueur :
essaie = 5          # Essaies restants pour l'utilisateur

# -- Mode 2 joueurs :
essaie_1 = 0        # Essaies restants pour le joueur 1
essaie_2 = 0        # Essaies restants pour le joueur 2
joueur_numero = 0   # Numéro du joueur qui doit jouer

# Choix du nombre de joueurs
nb_joueur = int(input("Entrez le nombre de joueurs (1 ou 2): "))

# On demande à l'uilisateur d'entrer un nombre (soit 1 soit 2) et on continue jusqu'à ce qu'il le fasse
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
    # On répète la boucle tant que l'utilisateur n'a pas trouvé la bombe et qu'il lui reste des essaies
    while essaie <= 5 and essaie >= 1:
        # On demande à l'utilisateur de rentrer une coordonnée entre 0 et 100 inclus
        user_co = int(input("Entrez un nombre entre 0 et 100 (inclus) : "))
        
        # On vérifie si la coordonnée donnée par l'utilisateur est comprise dans l'interval donné par l'utilisateur
        if (user_co <= l_co_bombe_max and user_co >= l_co_bombe_min):
            # Si c'est compris dedans alors on affiche une phrase de bravo
            print("Bravo ! Vous avez trouvé la bombe !")
            # Et on arrête la boucle
            break
        elif user_co == bombe:
            # Si c'est égal on affiche une phrase (bon c'est pas nécessaire mais c'est drôle)
            print("Waouw quel sniper ! Vous avez trouvé l'emplacement exact de la bombe !")
            
            # Et on arrête la boucle
            break
        else:
            # Sinon on affiche une phrase de déception et on enlève 1 aux essaies restants
            print("Raté ! Il vous reste", str(essaie-1), "tentatives !")
            essaie -= 1

    # Si l'utilisateur n'a plus d'essaies alors on fait exploser la bombe
    if essaie == 0:
        print("1\nBOOM ! La bombe était placée en " + str(bombe) + " !")

    # Sinon on affiche juste les coordonnées de la bombe
    else:
        print("La bombe était placée en " + str(bombe) + " !")


# Mode deux joueurs
elif nb_joueur == 2:
    # On fixe les essaies des deux joueurs à 5
    essaie_1 = 5
    essaie_2 = 5
    
    # On créé une boucle qui fonctionnera nb_joueur*2 fois
    for loop in range(nb_joueur * 2):
        # Tour du joueur 1
        joueur_numero = 1
        print("\nJoueur " + str(joueur_numero) + ", prépare toi !\nC'est partiii !!")
        # On demande au joueur 1 de choisir un nombre entre 0 et 100 inclus
        user_co = int(input("Entrez un nombre entre 0 et 100 : "))
        
        if (user_co <= l_co_bombe_max and user_co >= l_co_bombe_min):
            # Si le nombre qu'il a donné est compris dans l'interval de la bombe alors on affiche une phrase de bravo
            print("Bravo joueur " + str(joueur_numero) + "! Tu as trouvé la bombe !")
            # Et on arrête la boucle
            break
        elif user_co == bombe:
            # Si c'est égal on affiche une phrase (bon c'est pas nécessaire mais c'est drôle)
            print("Waouw quel sniper " + str(joueur_numero) + " ! Vous avez trouvé l'emplacement exact de la bombe !")
            # Et on arrête la boucle
            break
        else:
            # Sinon on affiche le nombre d'essaies restants au joueur 1
            print("Raté joueur " + str(joueur_numero) + " ! Il te reste", str(essaie_1-1), "tentatives !")
            # Et on lui elève un essaie au joueur 1
            essaie_1 -= 1
        
        # Tour du joueur 2
        joueur_numero = 2
        print("\nJoueur " + str(joueur_numero) + ", prépare toi !\nOn y go !!")
        # On demande au joueur 2 de choisir un nombre entre 0 et 100 inclus
        user_co = int(input("Entrez un nombre entre 0 et 100 : "))
        
        if (user_co <= l_co_bombe_max and user_co >= l_co_bombe_min):
            # Si le nombre qu'il a donné est compris dans l'interval de la bombe alors on affiche une phrase de bravo
            print("Bravo joueur " + str(joueur_numero) + "! Tu as trouvé la bombe !")
            # Et on arrête la boucle
            break
        elif user_co == bombe:
            # Si c'est égal on affiche une phrase (bon c'est pas nécessaire mais c'est drôle)
            print("Waouw quel sniper " + str(joueur_numero) + " ! Vous avez trouvé l'emplacement exact de la bombe !")
            # Et on arrête la boucle
            break
        else:
            # Sinon on affiche le nombre d'essaies restants au joueur 2
            print("Raté joueur " + str(joueur_numero) + " ! Il te reste", str(essaie_2-1), "tentatives !")
            # Et on enlève 1 essaie au joueur 2
            essaie_2 -= 1
        
    
        # Si les deux joueurs n'ont pas trouvé :
        if essaie_1 == 0 or essaie_2 == 0:
            # On exécute la fonction explode() qui permet de "faire exploser" la bombe
            print("1\nBOOM ! La bombe était placée en " + str(bombe) + " !")
            # Et on arrête la boucle
            break
    # On affiche la position de la bombe
    print("La bombe était placée en " + str(bombe) + " !")
