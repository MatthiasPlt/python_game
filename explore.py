import random
from creatures_model import Creature
from location import Item
from combat import combat

# Liste des monstres possibles
monsters = [
    {"name" : "Silva","races": "Gobelin", "health": 50, "attack": 8, "defense" : 10, "armor": 3, "level": 1, "xp": 30},
    {"name" : "Uzuma", "races": "Squelette", "health": 60, "attack": 10, "defense" : 15, "armor": 5, "level": 2, "xp": 40},
    {"name" : "Suke", "races": "Orc", "health": 100, "attack": 15, "defense" : 17,"armor": 10, "level": 3, "xp": 60},
    {"name" : "Lorni", "races": "Dragon", "health": 200, "attack": 30, "defense" : 30,"armor": 20, "level": 5, "xp": 100},
]

def random_monster():
    # Choisir un monstre aléatoire de la liste
    monster_info = random.choice(monsters)
    return Creature(**monster_info)

def explore(player, current_location):
    print(current_location.get_description())
    
    # Événements aléatoires
    event = random.choice(["monster", "item", "nothing"])
    
    if event == "monster":
        # Créer un monstre aléatoire
        enemy = random_monster()
        enemy.creature_appearing()
        print(f"Un {enemy.name} surgit ! Préparez-vous au combat.")
        combat(player, enemy)
    elif event == "item":
        item = Item(name="Potion de soin", effect="heal")
        print(f"Vous trouvez un objet : {item.name} !")
        player.inventory.append(item)
    else:
        print("Rien d'intéressant ici.")