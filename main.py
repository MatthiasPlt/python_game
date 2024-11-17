from player import Player
from location import Location
from game_loop import game_loop
from load_game import load_game  # Pour charger une sauvegarde
from setup_location import setup_locations
import sys

def show_menu():
    """Affiche le menu principal."""
    print("Bienvenue dans notre jeu d'aventure !")
    print("1 : Commencer une nouvelle partie")
    print("2 : Charger une partie sauvegardée")
    print("3 : Quitter le jeu")
    
    choice = input("Choisissez une option : ").strip()
    return choice



def new_game():
    """Initialise une nouvelle partie et retourne le joueur et son point de départ."""
    # Initialiser le lieu de départ
    starting_location = setup_locations()

    # Créer le joueur
    name = input("Entrez le nom de votre héros : ")
    player = Player(name, starting_location)

    return player, starting_location




def load_game_option():
    """Permet de charger une partie sauvegardée."""
    try:
        player = load_game()  # Charger le joueur depuis une sauvegarde
        print(f"\nPartie chargée. Bienvenue de retour, {player.name} !")
        # Charger la dernière position du joueur
        starting_location = Location("Forêt Sombre", "Lieu chargé de la sauvegarde.")  # Placeholder
        return player, starting_location
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None, None

def main():
    while True:
        choice = show_menu()
        
        if choice == "1":
            player, current_location = new_game()
        elif choice == "2":
            player, current_location = load_game_option()
        elif choice == "3":
            print("Merci d'avoir joué ! À bientôt.\n")
            sys.exit()
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.\n")
            continue 
        
        game_loop(player, current_location)

        # Après un Game Over, demander si le joueur veut recommencer ou quitter
        restart_choice = input("Voulez-vous recommencer ? (oui/non) : ").strip().lower()
        if restart_choice != "oui":
            print("Merci d'avoir joué ! À bientôt.")
            sys.exit()


if __name__ == "__main__":
    main()

