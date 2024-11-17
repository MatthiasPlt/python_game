import random
from combat import combat, boss_combat
from boss import Boss
from creat_monster import random_monster

class Location:
    def __init__(self, name, description, north=None, south=None, east=None, west=None, has_boss=False):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.has_boss = has_boss

    def get_description(self):
        return f"{self.name}\n{self.description}"

    def handle_event(self, player):
        # Vérifier si l'emplacement a un boss
        if self.has_boss:
            print("Préparez-vous pour le combat final contre MATHIAS SOW !")
            boss = Boss("MATHIAS SOW", "Une créature massive avec des yeux brûlants.", 200, 25, 10)
            boss_combat(player, boss)
            # Une fois le combat terminé, désactiver le boss pour cet emplacement
            self.has_boss = False
            return

        # Si pas de boss, générer un événement aléatoire
        event = random.choice(["monster", "item", "nothing"])
        if event == "monster":
            # Créer un monstre aléatoire et lancer le combat
            enemy = random_monster()
            enemy.creature_appearing()
            print("\n")
            combat(player, enemy)
        elif event == "item":
            # Trouver un objet
            item = Item(name="Potion de soin", effect="heal")
            player.inventory.append(item)
            print(f"Vous trouvez un objet : {item.name} !\n")
        else:
            print("Rien d'intéressant ici.\n")



class Item:
    def __init__(self, name, effect=None):
        self.name = name
        self.effect = effect  # Peut être un soin ou autre

    def __str__(self):
        return self.name



