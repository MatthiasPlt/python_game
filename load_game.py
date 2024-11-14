import json
from player import Player

def save_game(player, filename="savefile.json"):
    with open(filename, 'w') as f:
        json.dump(player.__dict__, f)

def load_game(filename="savefile.json"):
    with open(filename, 'r') as f:
        data = json.load(f)
        return Player(**data)
