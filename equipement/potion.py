class Potion:
    def __init__(self, effect, touchennemi, efficaciti):
        self.effect = effect
        self.touchennemi = touchennemi
        self.efficaciti = efficaciti

    def get_effect_potion(self):
        return self.effect

    def get_touchennemi(self):
        return self.touchennemi

    def get_efficaciti(self):
        return self.efficaciti


