from combat import combat
from move import move

def explore(player, current_location):
    # Affiche la description de l'emplacement actuel
    print(current_location.get_description())
    
    # Gérer les événements à l'emplacement actuel
    if hasattr(current_location, 'handle_event'):
        current_location.handle_event(player)

    # Retourner la position actuelle pour synchronisation avec game_loop
    return player.location
