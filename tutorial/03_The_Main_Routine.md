# The Main Game Routine

So far, our game does not really possess any logic that could be executed. This will change now. After completing this tutorial, you will be able to start your Textadventure and issue the first commands. But first, let's have a look at the current implementation of `Textadventure.py`:

```py
class Textadventure:

    def __init__(self):
        self.world = World()
        self.player = Player()

    def main_loop(self):
        pass
```

To tell the Python interpreter what to do when we execute this file, we have to add the following construct to the bottom of the file:

```py
if __name__ == `__main__`:
    Textadventure()
```

This tells Python to create a new object of our class `Textadventure`, when we give it the `Textadventure.py` file to run:

```bash
> python3 Textadventure.py
```