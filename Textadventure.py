"""A rather basic text adventure."""

import sys
import os
import csv
from World import World
from Inventory import Inventory


class Textadventure:
    """Main class of the Textadventure game."""

    def __init__(self, name_player, name_game):
        self.w = World('{}_places.csv'.format(name_game.lower()))
        self.p = Player(name_player)
        self.welcome(name_player, name_game)
        self.main_loop()
    
    def main_loop(self):
        won = False
        while not won:
            print("Your current position is '{}'.".format(self.w.current_tile.name))
            print(self.w.current_tile.description)
            input_cmd = input("Input> ")
            input_cmd = input_cmd.split(" ")
            if input_cmd[0] in ['m', 'move']:
                self.w.move(input_cmd[1])
            elif input_cmd[0] in ['e', 'examine']:
                self.inventory.examine(input_cmd[1])
    
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
            print(" - Move around the world by entering 'move' followed by one of the four geographic directions 'north', 'east', 'south', or 'west'. You can also use only the first letters, so 'move east' and 'm e' are both valid inputs, while 'muf noarth' and 'a o' are not.")
            print("Now that you know the rules, let's begin the adventure! Have fun!")
        else:
            print("Well, then let's start right away! Have fun!")


class Player:
    """Player-class, that holds the current position, the inventory and the player stats."""

    def __init__(self, name: str):
        self.name = name
        self.inventory = Inventory()

    def move(self, direction: str):
        if direction not in ['n', 'e', 's', 'w']:
            print("Beep! This direction is not valid!")

if __name__ == '__main__':
    t = Textadventure('Jannis', 'Kappengasse')
