from random import randint
import curses
from Game_Objects.global_vars import MAX_X, MAX_Y


class Collectable():
    def __init__(self, window, char: chr, color_pair: int):
        self.x = randint(1, MAX_X - 1)  # Setting random Ox coordinate
        self.y = randint(1, MAX_Y - 1)  # Setting random Oy coordinate
        self.char = char  # represents obj on the screen
        self.window = window  # Choosing window
        self.color_pair = color_pair

    @property
    def coordinate(self):
        return self.x, self.y

    @coordinate.setter
    def coordinate(self, xy: tuple):
        self.x, self.y = xy[0], xy[1]

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)

    def render(self):
        self.window.addstr(self.y, self.x, self.char, curses.color_pair(self.color_pair))
