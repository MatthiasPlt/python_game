# creatures.py

class Creature:
    def __init__(self, name, races, health, armor, attack, defense, level, xp):
        self.name = name  # Nom de la créature
        self.races = races  # Type ou race de la créature (ex: gobelin, squelette, etc.)
        self.level = level  # Niveau de la créature
        self.defense = defense # Niveau de la créature en defense
        self.health = health  # Points de vie
        self.armor= armor # Armure
        self.attack = attack  # Attaque
        self.xp = xp  # Points d'expérience à obtenir après sa défaite

    def creature_appearing(self):
        """Affiche quand une créature apparaît"""
        print(f"Un {self.name} ({self.races}) de niveau {self.level} apparaît avec {self.health} PV.")

    def death_creature(self):
        """Affiche le message de victoire après avoir tué la créature"""
        print(f"Vous avez vaincu un {self.name} de niveau {self.level}. Vous gagnez {self.xp} points d'expérience.")

    def damage_creature(self, damage):
        """Applique des dégâts à la créature, en prenant en compte son armure"""
        # Calcul de la réduction des dégâts par l'armure
        reduced_damage = max(0, damage - self.armor)
        self.health -= reduced_damage
        print(f"{self.name} subit {reduced_damage} points de dégâts. Il lui reste {self.health} PV.")
        
        if self.health <= 0:
            self.death_creature()

    def attack(self, player):
        # Cette méthode calcule l'attaque de la créature
        damage = self.attack_value - player.armor  # Calcul des dégâts en fonction de l'armure du joueur
        if damage > 0:
            player.health -= damage
            print(f"{self.races} attaque {player.name} et inflige {damage} points de dégâts.")
        else:
            print(f"{self.races} attaque {player.name}, mais l'armure bloque tous les dégâts.")

    def death_creature(self):
        print(f"Vous avez vaincu un {self.races} de niveau {self.level} et gagnez {self.xp} XP.")


    def update_stats(self):
        """Mise à jour des caractéristiques d'une créature selon son niveau"""
        if self.level == 1:
            pass  # Pas de changement pour le niveau 1
        elif self.level > 1 and self.level <= 10:
            self.health += self.level * 30
            self.attack += self.level * 15
            self.armor += self.level * 10
        else:
            print("Erreur : Niveau de la créature invalide.")

class Boss(Creature):
    def __init__(self, name, races, health, attack, armor, level, xp, number_lives=3):
        super().__init__(name, races, health, attack, armor, level, xp)
        self.number_lives = number_lives  # Nombre de vies restantes

    def perte_life(self):
        """Gère la perte de vie du boss et la transition entre les phases"""
        if self.health <= 0:
            self.number_lives -= 1
            print(f"Le {self.name} a perdu une vie.")
            if self.number_lives == 0:
                print(f"Vous avez vaincu {self.name} !")
            elif self.number_lives == 2:
                print(f"Le {self.name} entre dans la phase 2. Il devient plus puissant.")
                self.health += 300
                self.attack += 50
            elif self.number_lives == 1:
                print(f"Le {self.name} entre dans la phase finale, il est plus dangereux !")
                self.armor += 300

    def damage_creature(self, damage):
        """Applique des dégâts à un boss, en prenant en compte ses vies restantes"""
        reduced_damage = max(0, damage - self.armor)
        self.health -= reduced_damage
        print(f"{self.name} (Boss) subit {reduced_damage} points de dégâts. Il lui reste {self.health} PV.")
        
        if self.health <= 0:
            self.perte_life()
