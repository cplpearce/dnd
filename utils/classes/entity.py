# pylint: disable=invalid-name
"""This class file contains the Entity class"""
import random


class Entity:
    """This class contains the Entity class"""

    def __init__(self, name, hitpoints, attack_bonus, damage_die, damage_bonus):
        """Initialize the base entity"""
        self.name = name
        self.ac = 10
        self.hitpoints = hitpoints
        self.attack_bonus = attack_bonus
        self.damage_die = damage_die
        self.damage_bonus = damage_bonus
        self.inventory = []

    def attack(self, target):
        """Attack another entity and subtract damage from target's hitpoints"""

        # get the result of the die roll
        hit_result = random.randint(1, 20) + self.attack_bonus

        # if the result is higher than the target's AC, then we hit
        print(f"{self.name} attacks {target.name} with an attack of {hit_result}...")
        if hit_result > target.ac:

            # now we calc the damage
            damage_result = random.randint(
                1, self.damage_die) + self.damage_bonus

            print(f"And hits! For {damage_result} damage!")

            # reduce enemy hitpoints
            target.hitpoints -= damage_result

        else:
            print("And misses!")
            print()

    def is_alive(self):
        """Is the entity alive?"""
        return self.hitpoints > 0

    # this @property means we can GET something, and we alias hitpoints to hp
    @property
    def hp(self):
        """Get the entity hitpoints"""
        return self.hitpoints

    # this @setter property decorator means we can SET its hp using this alias

    @hp.setter
    def hp(self, damage):
        self.hitpoints += damage

    @property
    def inventory(self):
        """Get the entity hitpoints"""
        return self.inventory

    @inventory.setter
    def add_to_inventory(self, item):
        self.inventory.append(item)
        return f"Added {item.name} to inventory"

    @inventory.setter
    def remove_from_inventory(self, item):
        self.inventory.remove(item.uid)

    def __str__(self):
        return f"{self.name} has {self.hitpoints} hitpoints"
