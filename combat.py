def combat(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        print("\nTour du joueur :")
        player.attack(enemy)
        if enemy.hp <= 0:
            print("Victoire du joueur !")
            break

        print("\nTour de l'ennemi :")
        enemy.attack(player)
        if player.hp <= 0:
            print("Défaite...")
            break
