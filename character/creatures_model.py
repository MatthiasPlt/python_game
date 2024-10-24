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

    def hp_creature(self):
        if self.level == 1:
            self.health = self.health
        elif self.level <= 0:
            print('erreur de la cration de la creature')
        elif self.level > 15:
            print('erreur de la cration de la creature')
        elif 2 <= self.level <= 15:
            self.health = self.health + self.level * 30

    def attack_creature(self):
        if self.level == 1:
            self.attack = self.attack
        elif 2 <= self.level <= 15:
            self.attack = self.attack + self.level * 15

    def armor_creature(self):
        if self.level == 1:
            self.armor = self.armor
        elif 2 <= self.level <= 15:
            self.armor = self.armor + self.level * 10






