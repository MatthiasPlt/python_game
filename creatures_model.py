import weapons
class Creature:
    def __init__(self, races, health, attack, armor, level, xp):
        self.races = races
        self.level = level
        self.health = health
        self.attack = attack
        self.armor = armor
        self.xp = xp

    def creature_appearing(self):
        print("Un", self.races, "de niveau", self.level, "apparait avec", self.health, "PV")

    def death_creature(self):
        print("vous avez vaincu un", self.races, "de niveau", self.level, "vous avez donc gagner",
              self.xp, "points d'experiences")
        '''players.xp += self.xp
        print("vous etes level ", level.players, "il vous manque donc ", xp_manquant, " points d'experiences avant le niveau sup")
        entre guillemets car players pas fait'''

    def damage_creature(self, Weapons):
        if self.armor > 0:
            weapons.Weapons.get_dps(12) %= 2

    def caracteristique_creature(self):
        if self.level == 1:
            self.health = self.health
            self.attack = self.attack
            self.armor = self.armor
        elif self.level <= 0 or self.level > 10:
            print('erreur de la cration de la creature')
        elif 2 <= self.level <= 10:
            self.health = self.health + self.level * 30
            self.attack = self.attack + self.level * 15
            self.armor = self.armor + self.level * 10


class Boss(Creature):
    def __init__(self, races, health, attack, armor, numberLife, xp):
        super().__init__(races, health, attack, armor, numberLife, xp)
        self.numberLife = 3

    def perte_life(self):
        if self.health <= 0:
            self.numberLife -= 1
            if self.numberLife == 0:
                print("vous avez vainque le dragon !!!")
            elif self.numberLife == 2:
                print("vous etes dans la phase 2, le dragon s'enerve et se renforce")
                print("il gagne 300 points de vie et 50 d'attaque en plus")
            elif self.numberLife == 1:
                print("vous etes dans la derniere phase, le dragon est furieux")
                print("il gagne 300 points d'armure")

    def boss(self):
        if self.numberLife == 3:
            self.health = self.health
            self.armor = self.armor
            self.attack = self.attack
        elif self.numberLife == 2:
            self.health += 300
            self.attack += 50
        elif self.numberLife == 1:
            self.armor += 300


'''
Creature("squelette", 150, 25, 50, 1, 10)
Creature("sorcier", 200, 30, 15, 1, 25)
Creature("invocateur", 250, 50, 0, 1, 50)
Creature("golem", 300, 15, 200, 1, 100)
Boss("Dragon", 700, 150, 0, 3, 5000)
'''
