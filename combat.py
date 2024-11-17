import sys


def combat(player, enemy):
    """Gère un combat contre un ennemi standard."""
    print(f"\n--- Combat entre {player.name} et {enemy.races} commence ! ---")
    while player.is_alive() and enemy.is_alive():
        # Tour du joueur
        print(f"\nTour de {player.name} :")
        if player.attack_value > enemy.armor:
            damage = player.attack_value - enemy.armor
            enemy.health -= damage
            print(f"{player.name} attaque {enemy.races}, infligeant {damage} dégâts.")
        else:
            print(f"{player.name} attaque {enemy.races}, mais l'armure de {enemy.races} bloque tous les dégâts.")
        
        if enemy.health <= 0:
            print(f"{enemy.races} est vaincu !")
            enemy.death_creature()
            return  # Fin du combat
        
        # Tour de l'ennemi
        print(f"\nTour de {enemy.races} :")
        enemy.attack(player)
        
        if player.health <= 0:
            print(f"{player.name} a été vaincu par {enemy.races}.")
            return  # Fin du combat
    
    print("\n--- Fin du combat ---")


def boss_combat(player, boss):
    """Gère un combat final contre un boss."""
    print(f"\n=== Combat final contre {boss.name} ===")
    print(f"{boss.name} ({boss.description}) se dresse devant vous.")
    
    while player.is_alive() and boss.is_alive():
        # Tour du joueur
        print(f"\nTour de {player.name} :")
        damage_to_boss = max(player.attack_value - boss.armor, 0)
        boss.take_damage(damage_to_boss)
        print(f"{player.name} attaque {boss.name}, infligeant {damage_to_boss} dégâts.")
        
        if not boss.is_alive():
            print(f"\n>>> Félicitations ! Vous avez vaincu {boss.name} ! <<<")
            break
        
        # Tour du boss
        print(f"\nTour de {boss.name} :")
        damage_to_player = boss.attack
        player.hp -= damage_to_player
        print(f"{boss.name} attaque {player.name}, infligeant {damage_to_player} dégâts.")
        
        if not player.is_alive():
            print("\n>>> Vous avez été vaincu par le boss... <<<")
            break
    sys.exit()

    # Résumé final après le combat
    print("\n=== Fin de l'aventure ===")
    if player.is_alive():
        print("Vous avez triomphé du boss et terminé votre quête avec bravoure !")
    else:
        print("Le boss a triomphé. Votre aventure prend fin ici...")



