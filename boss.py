class Boss:
    def __init__(self, name, description, health, attack, defense, armor = 100):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.defense = defense
        self.armor = armor

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = max(self.attack - player.defense, 0)
        player.health -= damage
        print(f"{self.name} attaque {player.name} et lui inflige {damage} de dégâts !")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} subit {damage} de dégâts !")


