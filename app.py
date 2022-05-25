"""This is the base script to launch the game"""

from .scripts.classes.entity import Entity

max_the_hero = Entity("Max", 100, 10)

max_the_hero.attack(Entity("John", 100, 10))
