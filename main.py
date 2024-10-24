from character import creatures_model
import menu
from character.creatures_model import Creature
menu.menu()
Squellette = Creature("Squellette", 100, 50, 10, 1, 20)
Squellette.creature_appearing()
Squellette.death_creature()