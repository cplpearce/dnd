class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return f"{self.name} has {self.hp} HP and does {self.damage} damage"
