import random
from creatures_model import Creature
from location import Item
from combat import combat

def explore(player, current_location):
    print(current_location.get_description())
    
    # Événements aléatoires
    event = random.choice(["monster", "item", "nothing"])
    
    if event == "monster":
        enemy = Creature(name="Gobelin", attaque=8, defense=3, hp=30)
        print(f"Un {enemy.name} surgit ! Préparez-vous au combat.")
        combat(player, enemy)
    elif event == "item":
        item = Item(name="Potion de soin", effect="heal")
        print(f"Vous trouvez un objet : {item.name} !")
        player.inventory.append(item)
    else:
        print("Rien d'intéressant ici.")