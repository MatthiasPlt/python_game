import creatures_model


class Weapons:
    def __init__(self, variete, level=1, dps=50, bonus=None):
        """
        Initialisation d'une arme.
        - variete : Type de l'arme (couteau, hache, épée, etc.).
        - level : Niveau de l'arme, doit être entre 1 et 10.
        - dps : Dégâts par seconde de l'arme.
        - bonus : Bonus associé à l'arme.
        """
        self.variete = variete
        self.level = level
        self.dps = dps
        self.bonus = bonus or {}

        # Validation du niveau de l'arme
        if not (1 <= self.level <= 10):
            raise ValueError("Le niveau de l'arme doit être entre 1 et 10.")

        # Mise à jour du DPS en fonction du niveau
        self.calculate_dps()

    def calculate_dps(self):
        """Recalcule le DPS en fonction du niveau."""
        base_dps = self.dps
        self.dps = base_dps + (self.level - 1) * 50

    def get_dps(self):
        """Retourne le DPS actuel de l'arme."""
        return self.dps

    def knife(self):
        """Crée un couteau."""
        return Weapons(variete='couteau', level=1, dps=100)

    def axe(self, level=1):
        """Crée une hache."""
        return Weapons(variete='hache', level=level, dps=150)

    def sword(self, level=1):
        """Crée une épée."""
        return Weapons(variete='épée', level=level, dps=200)

    def __str__(self):
        """Affiche les informations de l'arme."""
        return (f"Arme: {self.variete}, Niveau: {self.level}, "
                f"DPS: {self.dps}, Bonus: {self.bonus}")
