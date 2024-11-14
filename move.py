from explore import explore

def move(player, current_location):
    command = input("Que voulez-vous faire ? (ex: 'go north') : ").strip().lower()
    
    if command.startswith("go "):
        direction = command.split(" ")[1]
        if direction in current_location.exits:
            return current_location.exits[direction]
        else:
            print("Vous ne pouvez pas aller dans cette direction.")
    else:
        print("Commande inconnue.")
    return current_location