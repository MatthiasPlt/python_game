import character.creatures_model


class Weapons:
    def __init__(self, variete, level, dps, bonus):
        self.variete = variete
        self.level = level
        self.dps = dps
        self.bonus = bonus

    def get_dps(self):
        return self.dps
    def level(self):
        if self.level <= 0 or self.level >= 11:
            print("erreur lors de la creation de l'armes")
        elif self.level == 1:
            self.dps = self.dps
        else:
            self.dps += self.level * 50

    def knife(self, variete, name, dps):
        self.variete = 'couteau'
        self.level = 1
        self.dps = 100

    def axe(self):
        self.variete = 'hache'
        self.level = self.level
        self.dps = 150

    def sword(self):
        self.variete = 'épé'
        self.level = self.level