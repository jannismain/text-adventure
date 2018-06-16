# A Text Adventure in Python

![](docs/screencap.gif)

## Already Implemented

- [x] Load Textadventure `World` from `csv` file
- [x] Load `Items` from `csv` file
- [x] Let `Player` navigate the `World` (e.g. `move north`)
- [x] Print `Tile` description and surrounding on each turn
- [x] Let `Player` examine his own `Inventory` (`inventory`)
- [x] Assign `Items` to `Tiles` through `GlobalInventory`

## Future Ideas

- [ ] Add `Barriers` between `Tiles` to restrict `Players` access to some areas
- [ ] Let `Player` take items and put them in his `Inventory`
- [ ] Let `Player` use items on other `Items` or `Barriers`
- [ ] Add option to save game and load previously saved games on start
- [ ] Add `NPC` to `World` for `Player` to interact with (`talk`)
  - [ ] NPCs should be able to have a (branching) dialogue with the `Player`
  - [ ] NPCs should be able to take / interact with `Items` (`use` | `show`)
  - [ ] NPCs should be able to follow the `Player` across `Tiles` (as option in dialogue)
- [ ] Add color to terminal output
  - [ ] [colorama](https://pypi.org/project/colorama/)
  - [ ] [Relevant SO question](https://stackoverflow.com/questions/287871)
- [ ] Define Goal of Game in csv files
    - Possible Goals:
        - Reach special tile
        - Obtain special item

## Tutorial
As my girlfriend wanted to know, how one would go about implementing something like this, I started to assemble a tutorial that covers all the things I used in this project so far. I would say it is targeted towards people who want to learn Python as their first programming language. If you are interested, check it out [here](tutorial/00_Overview).

## Related

* http://www.ifarchive.org
* http://brasslantern.org/writers/
* https://inventwithpython.com/blog/2014/12/11/making-a-text-adventure-game-with-the-cmd-and-textwrap-python-modules/
* https://gist.github.com/sma/2391632
* https://www.python-forum.de/viewtopic.php?t=29056
