from player import Player
from location import Location
from game_loop import game_loop
from load_game import load_game  # Pour charger une sauvegarde
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
    """Initialise une nouvelle partie avec des lieux et un joueur."""
    print("\n=== Nouvelle Partie ===")
    player_name = input("Entrez le nom de votre héros : ")
    player = Player(name=player_name)

    # Création des lieux
    forest = Location("Forêt Sombre", "Des arbres denses vous entourent.")
    cave = Location("Caverne Humide", "Une odeur de moisissure emplit l'air.")
    lake = Location("Lac Mystique", "L'eau scintille sous la lumière de la lune.")
    
    # Configuration des connexions
    forest.add_exit("north", cave)
    cave.add_exit("south", forest)
    forest.add_exit("east", lake)
    lake.add_exit("west", forest)
    
    return player, forest  # Le joueur commence dans la forêt

def load_game_option():
    """Permet de charger une partie sauvegardée."""
    try:
        player = load_game()
        print(f"\nPartie chargée. Bienvenue de retour, {player.name} !")
        # Vous devez également gérer la position actuelle dans le jeu
        # Exemple: retourne la position sauvegardée
        starting_location = Location("Forêt Sombre", "Lieu chargé de la sauvegarde.")  # Placeholder
        return player, starting_location
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None, None

def main():
    """Point d'entrée principal du jeu."""
    player = None
    current_location = None
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            player, current_location = new_game()
            break  # Passe à la boucle de jeu
        elif choice == "2":
            player, current_location = load_game_option()
            if player and current_location:
                break  # Passe à la boucle de jeu
        elif choice == "3":
            print("Merci d'avoir joué ! À bientôt.")
            sys.exit()
        else:
            print("Choix invalide, veuillez réessayer.")
    
    # Démarrage de la boucle principale du jeu
    game_loop(player, current_location)

if __name__ == "__main__":
    main()
