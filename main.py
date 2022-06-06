"""This is the base script to launch the game"""

# import classes
from adventurelib import when, start
# from utils.classes.entity import Entity


# handle player actios
@when("inventory")
@when("i")
def inventory():
    """Command to show the inventory"""
    print("You check your inventory.")
    # print user inventory


if __name__ == "__main__":
    start()
