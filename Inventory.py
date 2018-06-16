import csv
import logging

import Player


class Inventory:
    """Inventory class for Textadventure."""

    def __init__(self, owned_by, size: int = 10):
        self.owner = owned_by
        self.items = []
        self.size = size

    def check_inventory(self):
        print(self.inventory)

    def add(self, item: str, silent: bool=False):
        """Add items to your inventory."""
        if len(self.items) < self.size:
            self.items.append(item)
            if not silent:
                print(f"You added {item} to your inventory!")
        else:
            print("Your inventory is full. Discard an item before you can add new ones!")

    def remove(self, item: str):
        """Remove items from your inventory."""
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Beep! {item} is not in your inventory!")

    def exists(self, item_name: str):
        return item_name in [str(item_name) for item_name in self.items]

    def get_item(self, item_name: str) -> list:
        return [item for item in self.items if item.name == item_name]

    def __str__(self):
        if len(self.items) == 0:
            return "Your Inventory is empty!"
        elif isinstance(self.owner, Player.Player):
            return f"Inventory: {str(self.items)}"
        else:
            return f"{self.owner}: {str(self.items)}"

    def __repr__(self):
        return self.__str__()


class GlobalInventory(Inventory):
    """Hold all items available in the Textadventure's `World`."""

    def __init__(self, datafile, world=None, player=None):
        super().__init__(owned_by=None, size=999)
        self.items = self.load(datafile)
        if world and player:
            self.distribute_items(world, player)

    def __str__(self):
        return super().__str__().replace("Inventory", "GlobalInventory", 1)

    @staticmethod
    def load(datafile: str):
        items = []
        with open(datafile) as csv_file:
            data = csv.reader(csv_file, delimiter=';')
            for datarow in data:
                try:
                    items.append(Item(*datarow))
                except AttributeError:
                    print('Beep! The item entry for {datarow[0]} does not provide sufficient information.')
                    print("A minimal item entry has the following four values: name, description, is_obtainable and it's start location.")
                except AssertionError:
                    print(
                        f"Beep! Place '{datarow[0]}' does not seem to be a valid item. It's initial location is not with the player and cannot be associated with any tile.")
        return items

    def distribute_items(self, world, player):
        for item in self.items:
            if item.location.lower() == 'player':
                player.inventory.add(item, silent=True)
            else:
                try:
                    world.get_tile(item.location).inventory.add(item, silent=True)
                except AttributeError:
                    logging.error(
                        'The initial location %s of %s cannot be associated with any tile.',
                        item.location,
                        item)


class Item:
    """An item represents an object in the `Inventory`."""

    def __init__(self, name: str, description: str, is_obtainable, start_location: str):
        self.name = name
        self.description = description
        self.is_obtainable = bool(int(is_obtainable))
        self.location = start_location
        self.error_msg = {
            "take": "It probably won't fit.",
            "default": "Now is not the time for this.",
        }

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    i = GlobalInventory('kappengasse_items.csv', None, None)
    print(i)
