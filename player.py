from location import Location


class Player:
    def __init__(self, name, location, health=50, attack=10, defense=5, hp=100, level=1):
        self.name = name
        self.health = health
        self.attack_value = attack
        self.defense = defense
        self.hp = hp
        self.max_hp = hp  # Point de vie maximum
        self.level = level
        self.experience = 0  # Expérience initiale
        self.inventory = []
        self.location = location

    def is_alive(self):
        """Retourne True si le joueur est encore en vie, False sinon."""
        return self.hp > 0    
    
    def attack(self, target):
        """Effectue une attaque sur un autre joueur ou monstre."""
        damage = self.attaque - target.defense
        if damage > 0:
            target.take_damage(damage)
            print(f"{self.name} attaque {target.name} et inflige {damage} dégâts.")
        else:
            print(f"{self.name} attaque {target.name}, mais l'attaque est trop faible pour faire des dégâts.")
    
    def take_damage(self, damage):
        """Réduit les points de vie en cas de dégâts reçus."""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} est vaincu !")
        else:
            print(f"{self.name} subit {damage} dégâts. Points de vie restants : {self.hp}/{self.max_hp}")
    
    def heal(self, amount):
        """Restaure des points de vie."""
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} récupère {amount} points de vie. PV actuels : {self.hp}/{self.max_hp}")
    
    def use_object(self, obj):
        """Utilise un objet de l'inventaire."""
        if obj in self.objects:
            print(f"{self.name} utilise {obj}!")
            # Exemple d'objets : 'Potion' pourrait soigner
            if obj == "Potion":
                self.heal(20)
            # Après utilisation, on enlève l'objet
            self.objects.remove(obj)
        else:
            print(f"{self.name} n'a pas {obj} dans son inventaire.")
    
    def gain_experience(self, amount):
        """Gagne de l'expérience et potentiellement monte de niveau."""
        self.experience += amount
        print(f"{self.name} gagne {amount} points d'expérience. Total : {self.experience}")
        while self.experience >= self.experience_to_next_level():
            self.level_up()
    
    def level_up(self):
        """Monte de niveau, améliore les statistiques."""
        self.level += 1
        self.experience -= self.experience_to_next_level()
        self.attaque += 2
        self.defense += 1
        self.max_hp += 10
        self.hp = self.max_hp
        print(f"Félicitations ! {self.name} monte au niveau {self.level} !")
        print(f"Nouvelle attaque : {self.attaque}, nouvelle défense : {self.defense}, nouveaux PV max : {self.max_hp}")
    
    def experience_to_next_level(self):
        """Calcule l'expérience nécessaire pour le prochain niveau."""
        return 100 * self.level
    
    def add_object(self, obj):
        """Ajoute un objet à l'inventaire."""
        self.objects.append(obj)
        print(f"{self.name} obtient {obj}.")
    
    def show_stats(self):
        """Affiche les statistiques du joueur."""
        print(f"Nom: {self.name}")
        print(f"PV: {self.hp}/{self.max_hp}")
        print(f"Attaque: {self.attaque}")
        print(f"Défense: {self.defense}")
        print(f"Niveau: {self.level}")
        print(f"Expérience: {self.experience}/{self.experience_to_next_level()}")
        print(f"Inventaire: {', '.join(self.objects) if self.objects else 'Vide'}")







