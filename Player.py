from Inventory import Inventory

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