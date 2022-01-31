import csv
import logging
import pathlib

from Inventory import Inventory

DIRECTIONS = {"n": "north", "e": "east", "s": "south", "w": "west"}


class World:
    """Word-class, that holds information about available tiles and items."""

    def __init__(self, game: str):
        self.tiles, self.current_tile = self.load(game)
        # replace tile's surroundings reference with actual Tiles
        [tile.discover_tiles(self) for tile in self.tiles]
        logging.debug(f"Loaded Tiles: {self.tiles}")

    @staticmethod
    def load(game_places: pathlib.Path):
        tiles = []
        start_at = ""
        if not game_places.exists():
            logging.error(
                f"Game '{game_places.parent.name}' doesn't define a '{game_places.name}'!"
            )
            exit(1)
        with game_places.open() as csv_file:
            data = csv.reader(csv_file)
            for datarow in data:
                try:
                    tiles.append(Tile(*datarow))
                except AttributeError:
                    print(
                        f"Beep! The description of {datarow[0]} does not provide sufficient information."
                    )
                    print(
                        "A minimal place description has the following 5 entries: name, north_exit, east_exit, south_exit, west_exit"
                    )
                    print(
                        "Additional entries are considered point of interests or items available for closer examination."
                    )
                except AssertionError:
                    print(
                        f"Beep! Place '{datarow[0]}' does not seem to be a valid place. It is not connected to any other tile at the moment."
                    )

                if datarow[0].endswith("*"):
                    if start_at == "":
                        start_at = tiles[-1]
                    else:
                        raise AttributeError(
                            "Data contains more than one start tile. Start tiles are indicated by a '*' at the end of a place name."
                        )
        return tiles, start_at

    def move(self, direction: str):
        """Move from the current tile in the specified direction (if valid)."""
        if len(direction) == 1:
            try:
                direction = DIRECTIONS[direction]
            except ValueError:
                print("Beep! {} is not a valid geographic direction!")
        new_tile = self.current_tile.surrounding[direction]
        if new_tile:
            self.current_tile = new_tile
            self.current_tile.visited = True
            print("You moved to '{}'.".format(self.current_tile.name))
        else:
            print("Beep! This move is not available!")

    def get_tile(self, name):
        for tile in self.tiles:
            if tile.name == name:
                return tile
        return None


class Tile:
    """A world contains many tiles."""

    def __init__(self, name, north, east, south, west, description=""):
        if name.endswith("*"):
            self.name = name[:-1]
            self.visited = True
        else:
            self.name = name
            self.visited = False
        self.description = description

        self.surrounding = {"north": north, "east": east, "south": south, "west": west}
        self.inventory = Inventory(self)
        self.test_tile_validity()

    @property
    def exits(self):
        return [dir for (dir, tile) in self.surrounding.items() if tile != None]

    def test_tile_validity(self):
        assert any([tile for tile in self.surrounding.items() if tile != "None"])

    def discover_tiles(self, world: World):
        for dir, tile_desc in self.surrounding.items():
            self.surrounding[dir] = world.get_tile(tile_desc)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    World(pathlib.Path(__file__).parent / "games" / "kappengasse" / "places.csv")
