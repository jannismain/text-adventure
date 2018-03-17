

class Inventory:
    """Inventory class for Textadventure."""

    def __init__(self, size: int = 10):
        self.inventory = []
        self.size = size

    def check_inventory(self):
        print(self.inventory)

    def add(self, item: str):
        """Add items to your inventory."""
        if len(self.inventory) < self.size:
            self.inventory.append(item)
            print("You added {} to your inventory!".format(item))
        else:
            print("Your inventory is full. Discard an item before you can add new ones!")

    def remove(self, item: str):
        """Remove items from your inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"Beep! {item} is not in your inventory!")

    def __str__(self):
        if len(self.inventory) == 0:
            return "Your Inventory is empty!"
        else:
            return f"Inventory: {str(self.inventory)}"

    def __repr__(self):
        return self.__str__()


class Item:
    """An item represents an object in the `Inventory`."""

    def __init__(self, name, description, is_obtainable):
        self.name = name
        self.description = description
        self.is_obtainable = is_obtainable

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
