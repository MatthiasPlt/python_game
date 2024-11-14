import random
from creatures_model import Creature
from combat import combat

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Dictionnaire pour les sorties, ex: {'north': location2}

    def add_exit(self, direction, location):
        self.exits[direction] = location

    def get_description(self):
        return f"{self.name}\n{self.description}"

class Item:
    def __init__(self, name, effect=None):
        self.name = name
        self.effect = effect  # Peut être un soin ou autre

    def __str__(self):
        return self.name



