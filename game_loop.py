from move import move
from explore import explore
from location import Location
from boss import Boss

def game_loop(player, current_location):
    while player.is_alive():
        current_location = explore(player, current_location)
        if current_location:  # Vérifie si le joueur est toujours à un emplacement valide
            move(player)
        else:
            print("Le jeu est terminé.")
            break



