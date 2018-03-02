import sys
import os
import csv


class World:
    """Word-class, that holds information about available tiles and items."""

    def __init__(self, data: str):
        self.tiles, self.current_tile = self.load(data)
        # print("Places: ", self.tiles)
        # print(self.current_tile)
    
    @staticmethod
    def load(datafile: str):
        tiles = []
        start_at = ""
        with open(datafile) as csv_file:
            data = csv.reader(csv_file)
            for datarow in data:
                try:
                    tiles.append(Tile(*datarow))
                except AttributeError:
                    print("Beep! The description of {} does not provide sufficient information.".format(datarow[0]))
                    print("A minimal place description has the following 5 entries: name, north_exit, east_exit, south_exit, west_exit")
                    print("Additional entries are considered point of interests or items available for closer examination.")
                except AssertionError:
                    print("Beep! Place {} does not seem to be a valid place. It is not connected to any other tile at the moment.")
                
                if datarow[0].endswith("*"):
                    if start_at == "":
                        start_at = tiles[-1]
                    else:
                        raise AttributeError("Data contains more than one start tile. Start tiles are indicated by a '*' at the end of a place name.")
        return tiles, start_at
    
    def move(self, direction: str):
        """Move from the current tile in the specified direction (if valid)."""
        if len(direction) == 1:
            try:
                direction = self.get_full_direction(direction)
            except ValueError:
                print("Beep! {} is not a valid geographic direction!")
        a = getattr(self.current_tile, direction)
        new_tile = self.get_tile(a)
        if new_tile:
            self.current_tile = new_tile
            print("You entered '{}'.".format(self.current_tile.name))
        else:
            print("Beep! This move is not available!")
    
    @staticmethod
    def get_full_direction(direction: str):
        if direction == 'n':
            return 'north'
        elif direction == 'e':
            return 'east'
        elif direction == 's':
            return 'south'
        elif direction == 'w':
            return 'west'
        else:
            raise ValueError("{} is not a valid direction.".format(direction))
    
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
        else:
            self.name = name
        self.description = description

        self.north = north
        self.east = east
        self.south = south
        self.west = west

        self.test_tile_validity()
    
    def test_tile_validity(self):
        assert(any([self.north, self.east, self.south, self.west]))

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    import sys
    World('kappengasse_places.csv')