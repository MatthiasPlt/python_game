from move import move
from explore import explore

def game_loop(player, current_location):
    """Boucle principale du jeu."""
    while player.hp > 0:
        print(f"\nVous êtes actuellement à : {current_location.name}")
        
        # Déplacer ou explorer
        current_location = move(player, current_location)
        explore(player, current_location)
    
    print("Game Over. Vous avez succombé à vos blessures.")
