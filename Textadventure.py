"""A rather basic text adventure."""

import sys
import os
import csv
import logging
import argparse

from World import World
from Player import Player
from Terminal import *


__version__ = 0.1


class Textadventure:
    """Main class of the Textadventure game."""

    def __init__(self, name_player: str, name_game: str):
        name_player, name_game = self.welcome(name_player, name_game)
        self.w = World(f'{name_game.lower()}_places.csv')
        self.p = Player(name_player)
        self.i = GlobalInventory(f'{name_game.lower()}_items.csv', world=self.w, player=self.p)
        self.main_loop()

    def main_loop(self):
        won = False
        print(f"Your current position is '{self.w.current_tile.name}'.")
        while not won:
            print(self.w.current_tile.description)
            # print(self.w.current_tile.inventory)
            print(f"""Exits are: {", ".join(self.w.current_tile.exits)}""")
            moved = False
            while not moved:
                user_input = inputn("> ").split(" ")
                if user_input[0] in ['l', 'look']:
                    for direction, tile in self.w.current_tile.surrounding.items():
                        if tile:
                            print(f"To the {direction} is '{tile}'", end="\n")
                elif user_input[0] in ['e', 'examine']:
                    if len(user_input) > 1:
                        item_name = " ".join(user_input[1:])
                        item = self.w.current_tile.inventory.get_item(item_name)
                        if not item:  # check inventory, if item cannot be found with Tile
                            item = self.p.inventory.get_item(item_name)
                        if item:
                            if input_cmd[0] in ['t', 'take']:
                                if item.is_obtainable:
                                    self.p.inventory.add(item)
                                else:
                                    print(f"You cannot take {item}. {item.error_msg['take']}")
                            elif input_cmd[0] in ['e', 'examine']:
                                print(item[0].description)
                        else:
                            print(f"Beep! {item_name} cannot be found here!")
                    else:
                        print(self.w.current_tile.inventory)
                elif user_input[0] in ['m', 'move']:
                    self.w.move(user_input[1])
                    moved = True
                elif user_input[0] in ['h', 'help']:
                    self.print_rules()
                elif user_input[0] in ['i', 'inventory']:
                    print(self.p.inventory)
                elif user_input[0] in ['q', 'quit']:
                    print("Do you really want go quit the game? [yes]|no")
                    if inputn("> ") in ['yes', 'y', '']:
                        exit()
                else:
                    print(
                        f"Beep! {input_cmd[0]} is not a command I recognize! Type 'help' to get a list of all available commands.")

    def welcome(self, name_player: str=None, name_game: str=None):
        clear()
        if not name_player:
            print("Welcome kind sir,")
            print("what is your name?")
            name_player = inputn("> ")
        print("Greetings {}! I am Alfred and I will be guiding you through a text adventure of your choosing.".format(name_player))
        if not name_game:
            print("What adventure do you want to embark on today?")
            name_game = inputn("> ")
        print("'{}'! What an excellent choice!".format(name_game))
        print("Do you already know how to play this game? [yes]|no")
        if inputn("> ") not in ['yes', 'y', '']:
            print("Then, let me tell you:")
            self.print_rules(header=False)
            print("Now that you know how to play this game, let's begin the adventure! Have fun!")
        else:
            print("Well, then let's start right away! Have fun!")
        print("\nPress ENTER to start the game...", end='')
        input('')  # keep separate, as input does appear immediately, while print simulates typing!
        clear()
        return name_player, name_game

    def print_rules(self, header=True):
        if header:
            print("GAMEPLAY:")
        print("- Move around the world by entering 'move' followed by either 'north', 'east', 'south', or 'west'.")
        print("- Look around your current location with 'look'.")
        print("- Examine certain objects with 'examine' followed by the object's name.")
        print("- Check your current inventory with 'inventory'.")
        print("- Take an item from the current location with 'take' followed by the item's name.")
        print("- PRO TIP: You can also use just the first letter for each command for faster gameplay!", end="\n\n")

    def print_surroundings(self):
        pass

    def get_item(self, item_name) -> Item:
        """Retrieve item from different Inventories.

        Look for *item_name* in `Player` inventory. If no item with *item_name* is found, look in the inventory of the current `Tile`.

        Returns:
            If item exists, return Item with *item_name*, otherwise return None.
        """
        for inventory in [self.p.inventory, self.w.current_tile.inventory]:
            item = inventory.get_item(item_name)
            if item and len(item) is 1:
                return item[0]
        return None


if __name__ == '__main__':
    import sys

    arg_handler = argparse.ArgumentParser(prog='Textadventure v{}'.format(__version__),
                                          description="A customizable Textadventure written in Python.",
                                          formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    arg_handler.add_argument('player_name', default=None, type=str, nargs='?', help='Your name')
    arg_handler.add_argument('-v', '--verbose', action='count', default=0, help='Enables logging')
    arg_handler.add_argument(
        'game_name',
        default=None,
        type=str,
        nargs='?',
        help='The name of the game you want to play')

    args = arg_handler.parse_args()
    if args.verbose > 0:
        logging.basicConfig(level=logging.DEBUG)
    t = Textadventure(args.player_name, args.game_name)
