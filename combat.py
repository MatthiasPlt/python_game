def combat(player, enemy):
    print("Tour du joueur :")
    # Si l'attaque du joueur est supérieure à l'armure de l'ennemi, infliger des dégâts
    if player.attack_value > enemy.armor:
        enemy.health -= player.attack_value - enemy.armor
        print(f"{player.name} attaque {enemy.races}, infligeant {player.attack_value - enemy.armor} dégâts.")
    else:
        print(f"{player.name} attaque {enemy.races}, mais l'armure de {enemy.races} bloque tous les dégâts.")

    if enemy.health <= 0:
        enemy.death_creature()
        return  # Fin du combat

    print("Tour de l'ennemi :")
    # L'ennemi attaque le joueur
    enemy.attack(player)
    
    if player.health <= 0:
        print(f"{player.name} a été vaincu par {enemy.races}.")
        return  # Fin du combat

