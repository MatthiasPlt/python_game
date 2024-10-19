class Creature:
    def __init__(self, races, health, attack, armor, level, xp):
        self.races = races
        self.health = health
        self.attack = attack
        self.armor = armor
        self.level = level
        self.xp = xp

    def get_races(self):
        return self.races

    def get_health(self):
        return self.health

    def get_level(self):
        return self.level

    def get_xp(self):
        return self.xp

    @staticmethod
    def creature_appearing():
        print(Creature.get_races, " de niveau", Creature.get_level, "apparait avec ", Creature.get_health, "PV")

    def death_creature(self):
        print("vous avez vaincu ", Creature.get_races, " de niveau ", Creature.get_level, " vous avez donc gagner", Creature.get_xp, "points d'experiences")
        '''players.xp += self.xp
        print("vous etes level ", level.players, "il vous manque donc ", xp_manquant, " points d'experiences avant le niveau sup")
        entre guillemets car players pas fait'''

    def damage_creature(self):
        if self.armor > 0:
            ''' j'attends la partie du jouers pour continuer'''



