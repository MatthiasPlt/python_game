class Creature:
    def __init__(self, name, races, health, armor, attack, defense, level, xp):
        self.name = name  # Nom de la créature
        self.races = races  # Type ou race de la créature (ex: gobelin, squelette, etc.)
        self.health = health  # Points de vie
        self.armor = armor  # Armure
        self.attack_value = attack  # Valeur d'attaque
        self.defense = defense  # Défense
        self.level = level  # Niveau de la créature
        self.xp = xp  # Points d'expérience accordés après sa défaite

    def is_alive(self):
        """Retourne True si la créature est encore vivante, sinon False."""
        return self.health > 0

    def creature_appearing(self):
        """Affiche un message lorsqu'une créature apparaît."""
        print(f"Un {self.name} ({self.races}) de niveau {self.level} apparaît avec {self.health} PV et {self.armor} armure.")

    def attack(self, player):
        """Effectue une attaque sur le joueur."""
        damage = max(0, self.attack_value - player.defense)  # Calcul des dégâts après défense
        if damage > 0:
            player.health -= damage
            print(f"{self.races} attaque {player.name}, infligeant {damage} points de dégâts.")
        else:
            print(f"{self.races} attaque {player.name}, mais l'armure bloque tous les dégâts.")

    def take_damage(self, damage):
        """Applique des dégâts à la créature, prenant en compte l'armure."""
        reduced_damage = max(0, damage - self.armor)  # Réduction par l'armure
        self.health -= reduced_damage
        if reduced_damage > 0:
            print(f"{self.name} subit {reduced_damage} dégâts. Il lui reste {max(self.health, 0)} PV.")
        else:
            print(f"L'attaque est trop faible pour percer l'armure de {self.name}.")
        if self.health <= 0:
            self.death_creature()

    def death_creature(self):
        """Affiche un message lorsque la créature meurt."""
        print(f"Vous avez vaincu un {self.races} de niveau {self.level} et gagnez {self.xp} XP.")

    def update_stats(self):
        """Met à jour les caractéristiques de la créature en fonction de son niveau."""
        if self.level == 1:
            pass  # Pas de changement pour le niveau 1
        elif 2 <= self.level <= 10:
            self.health += self.level * 30
            self.attack_value += self.level * 15
            self.armor += self.level * 10
            print(f"Stats mises à jour : {self.name} a {self.health} PV, {self.attack_value} attaque, et {self.armor} armure.")
        else:
            print("Erreur : Niveau de la créature invalide.")


