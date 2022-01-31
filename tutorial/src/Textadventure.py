from World import World
from Player import Player


class Textadventure:
    def __init__(self):
        self.world = World()
        self.player = Player()
        self.main_loop()

    def main_loop(self):
        pass


if __name__ == "__main__":
    Textadventure()
