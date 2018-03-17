"""A rather basic text adventure."""

import sys
import os
import csv
import time
import random
import logging

from World import World
from Inventory import Inventory, GlobalInventory

# TYPING_SPEED = 150  # wpm
# immediate_print = print


# def print(t, end="\n"):
#     for l in str(t):
#         sys.stdout.write(l)
#         sys.stdout.flush()
#         time.sleep(random.random() * 10.0 / TYPING_SPEED)
#     immediate_print('', end=end)


class Textadventure:
    """Main class of the Textadventure game."""

    def __init__(self, name_player, name_game):
        self.w = World(f'{name_game.lower()}_places.csv')
        self.p = Player(name_player)
        self.i = GlobalInventory(f'{name_game.lower()}_items.csv', world=self.w, player=self.p)
        self.welcome(name_player, name_game)
        self.main_loop()

    def main_loop(self):
        won = False
        print(f"Your current position is '{self.w.current_tile.name}'.")
        while not won:
            print(self.w.current_tile.description)
            print(self.w.current_tile.inventory)
            print(f"""Exits are: {", ".join(self.w.current_tile.exits)}""")
            moved = False
            while not moved:
                input_cmd = input("Input> ")
                input_cmd = input_cmd.split(" ")
                if input_cmd[0] in ['l', 'look']:
                    for direction, tile in self.w.current_tile.surrounding.items():
                        if tile:
                            print(f"To the {direction} is '{tile}'", end="\n")
                elif input_cmd[0] in ['e', 'examine']:
                    if len(input_cmd) > 1:
                        item_name = " ".join(input_cmd[1:])
                        item = self.w.current_tile.inventory.get_item(item_name)
                        if not item:  # check inventory, if item cannot be found with Tile
                            item = self.p.inventory.get_item(item_name)
                        if item:
                            print(item[0].description)
                        else:
                            print(f"Beep! {item_name} cannot be found here!")
                    else:
                        print(self.w.current_tile.inventory)
                elif input_cmd[0] in ['m', 'move']:
                    self.w.move(input_cmd[1])
                    moved = True
                elif input_cmd[0] in ['h', 'help']:
                    self.print_rules()
                elif input_cmd[0] in ['i', 'inventory']:
                    print(self.p.inventory)
                elif input_cmd[0] in ['q', 'quit', '']:
                    print("Do you really want go quit the game? [yes]|no")
                    if input("> ") in ['yes', 'y', '']:
                        exit()

    def welcome(self, name_player=None, name_game=None):
        if not name_player:
            print("Welcome kind sir,")
            print("what is your name?")
            name_player = input("> ")
        print("Greetings {}! I am Alfred and I will be guiding you through a text adventure of your choosing.".format(name_player))
        if not name_game:
            print("What adventure do you want to take on today?")
            name_game = input("> ")
        print("Ahh! I see... You want to play '{}'. What an excellent choice!".format(name_game))
        print("Are you already familiar with the rules? [yes]|no")
        if input("> ") not in ['yes', 'y', '']:
            print("Then, let me tell you how to play this game:")
            self.print_rules(header=False)
            print("Now that you know the rules, let's begin the adventure! Have fun!")
        else:
            print("Well, then let's start right away! Have fun!")

    def print_rules(self, header=True):
        if header:
            print(" + + +   R U L E S   + + +")
        print(" - Move around the world by entering 'move' follower by either 'north', 'east', 'south', or 'west'.")
        print(" - Look around your current location with 'look'.")
        print(" - Examine certain objects with 'examine' followed by the object's name.")
        print(" - Check your current inventory with 'inventory'.")
        print(" - Take an item from the current location with 'take' followed by the item's name.")
        print(" - PRO TIP: You can also use just the first letter for each command for faster gameplay!", end="\n\n")

    def print_surroundings(self):
        pass


class Player:
    """Player-class, that holds the current position, the inventory and the player stats."""

    def __init__(self, name: str, inventory_size: int = 10):
        self.name = name
        self.inventory = Inventory(owned_by=self, size=inventory_size)

    def move(self, direction: str):
        if direction not in ['n', 'e', 's', 'w']:
            print("Beep! This direction is not valid!")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    t = Textadventure('Jannis', 'Kappengasse')
