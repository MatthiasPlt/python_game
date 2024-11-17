def move(player):
    # Demander au joueur de choisir une direction
    direction = input("Que voulez-vous faire ? (ex: 'north', 'south', 'east', 'west') : ").strip().lower()

    current_location = player.location  # Accédez à l'emplacement actuel du joueur

    # Vérifier si la direction est valide
    if direction == "north" and current_location.north:
        player.location = current_location.north
        print(f"Vous vous déplacez vers le nord, vous êtes maintenant à {player.location.name}.")
    elif direction == "south" and current_location.south:
        player.location = current_location.south
        print(f"Vous vous déplacez vers le sud, vous êtes maintenant à {player.location.name}.")
    elif direction == "east" and current_location.east:
        player.location = current_location.east
        print(f"Vous vous déplacez vers l'est, vous êtes maintenant à {player.location.name}.")
    elif direction == "west" and current_location.west:
        player.location = current_location.west
        print(f"Vous vous déplacez vers l'ouest, vous êtes maintenant à {player.location.name}.")
    else:
        print("Vous ne pouvez pas aller dans cette direction.")

