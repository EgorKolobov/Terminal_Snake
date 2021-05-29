import curses
# ===============================================
# Dangerous spikes. If Snake hits them, it dies.


class Obstacle():
    def __init__(self, window, char: chr = 'X'):
        self.char = char  # represents Obstacle obj on the screen
        self.window = window  # choosing window
        self.exist = False  # checking non-existence
        self.rand = 0  # used in choosing random coordinates (see line 220)
        self.x = -1  # initial coordinates are outside of the window
        self.y = -1  # spike with such coordinates can't be rendered

    # Rendering spike
    def render(self):
        if self.exist:  # rendering only existing spikes
            self.window.addch(self.y, self.x, self.char)

    @property
    def coordinate(self):
        return self.x, self.y

    @coordinate.setter
    def coordinate(self, xy: tuple):
        self.x, self.y = xy[0], xy[1]
