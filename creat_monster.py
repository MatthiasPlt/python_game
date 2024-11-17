import random
from creatures_model import Creature

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
