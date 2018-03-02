

class Inventory:
    """Inventory class for Textadventure."""

    def __init__(self, size: int = 10):
        self.inventory = []
        self.size = size

    def check_inventory(self):
        print(self.inventory)

    def add(self, thing: str):
        """Add things to your inventory."""
        if len(self.inventory) < self.size:
            self.inventory.append(thing)
            print("You added {} to your inventory!".format(thing))
        else:
            print("Your inventory is full. Discard an item before you can add new ones!")

    def remove(self, thing: str):
        """Remove things from your inventory."""
        if thing in self.inventory:
            self.inventory.remove(thing)
        else:
            print("Beep! {} is not in your inventory!".format(thing))

class Thing:
    """Thing class for inventory."""
    
    def __init__(self, name):
        self.name = name