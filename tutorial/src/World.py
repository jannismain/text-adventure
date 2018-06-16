class World:

    def __init__(self):
        pass


class Tile:

    def __init__(self, name: str, description: str, *args):
        self.name = name
        self.description = description

        # either save surrounding tiles as list
        # self.surroundings = args
        # ... or save surrounding tiles as dictionary
        self.surroundings = {
            "north": args[0],
            "east": args[1],
            "south": args[2],
            "west": args[3]
        }
