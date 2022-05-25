"""This helper file contains various dice based helper functions"""
import random


def dice_roll(dice_type, dice_count):
    """
    This function rolls a dice and returns the result.
    :param dice_type: The type of dice to roll.
    :param dice_count: The number of dice to roll.
    :return: The result of the dice roll.
    """
    return random.randint(1, dice_type) * dice_count
