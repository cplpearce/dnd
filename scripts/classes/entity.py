"""This class file contains the Entity class"""

class Entity:
    """This class contains the Entity class"""
    def __init__(self, name, health, damage):
        """Initialize the base entity"""
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        """Attack another entity and subtract damage from target's health"""
        target.health -= self.damage
        print(f"{self.name} attacks {target.name} for {self.damage} damage")

    def is_alive(self):
        """Is the entity alive?"""
        return self.health > 0

    def __str__(self):
        return f"{self.name} has {self.health} health"
