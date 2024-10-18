import sys
def menu():
    print('bienvenue dans notre jeux')
    print("1 : commencer une nouvelle partie")
    print("2 : charger une partie sauvegardé")
    print("3 : detail d'une partie")
    print("4 : quitter le jeu")
    print('')

    choices_player = int(input("Choisissez ce que vous voulez faire: "))

    while choices_player < 1 or choices_player > 4:
        print('commande invalide')
        choices_player =  int(input('faites un autre choix :'))

    if choices_player == 1:
        print('ok1')
        ''' fonction de debut de la partie'''
    elif choices_player == 2:
        print('ok2')
        ''' relance la partie save'''
    elif choices_player == 3:
        print('ok3')
        ''' presentation du jeu'''
    else :
        print('fermeture du jeu')
        sys.exit("Message d'arrêt")
