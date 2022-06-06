# dnd

Max &amp; Clint's D&amp;D Game
This repo will be for a choose your own adenture game to help us learn python!

1. <s>Get base data</s>
2. Define text based engine



## Sample snippets
```python

# def start_game():
#     """Start the game"""

#     # get the user's name
#     hero_name = input("What is your name hero?.. ")

#     # check for user mashing enter
#     if not hero_name:
#         hero_name = "Hero"

#     # here we create the "hero" entity
#     player = Entity(hero_name, 8, 3, 8, 3)
#     # and a shitty goblin
#     enemy = Entity("Goblin", 3, 1, 4, 1)

#     # init a turn tracker
#     turns = 0

#     # start the battle
#     print()
#     print(f"The battle between {player.name} and the {enemy.name} begins!")

#     while player.is_alive():

#         # incrment the turn counter
#         turns += 1

#         turn_message = f"    Turn {turns}   "
#         line_decoration = "=" * len(turn_message)
#         print()
#         print(f"={line_decoration}=")
#         print(turn_message)
#         print(f"={line_decoration}=")
#         print()

#         # start by attacking the goblin
#         player.attack(enemy)

#         # check if its still alive
#         if not enemy.is_alive():
#             print()
#             print(f"!!!  {hero_name} kills the {enemy.name}  !!!")
#             print()
#             break

#         # it attacks back!
#         enemy.attack(player)

#         print("-----------------------------------------------")
#         print(f"{player.name} has {player.hp} hitpoints left!")


```