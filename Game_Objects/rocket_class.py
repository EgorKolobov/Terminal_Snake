import curses
from Game_Objects.global_vars import MAX_X, MAX_Y
from Game_Objects.hunter_class import Hunter

'''
Rocket. A dangerous projectile, which is used by Hunter.
If it hits Snake, Snake dies.
'''


class Rocket():
    def __init__(self, window, hunter, char: chr = '◈'):
        self.char = char  # represents Rocket on the screen
        self.window = window  # choosing window
        self.direction = 'DOWN'  # Rocket's initial direction
        self.exist = False  # allow to change direction(extremly important)
        self.draw = False  # allow to exist(super important)
        self.count = 0  # 20 frames 'time' delay
        self.first = True
        self.x = -1  # see commets in lines 207-209
        self.y = -1
        self.hunter = hunter

        self.rocket_moves = {
            'UP': self.go_up,
            'DOWN': self.go_down
        }

    def go_up(self):
        self.y -= 1
        if self.y < 1:
            self.y = MAX_Y

    def go_down(self):
        self.y += 1
        if self.y > MAX_Y:
            self.y = 1

    # Renders Rocket if it exists and 'time' delay is over
    def render(self):
        if self.draw and self.count == 20:
            self.window.addstr(self.y, self.x, self.char, curses.A_BOLD)

    # Changes Rocket direction if it's allowed to change direction
    def change_direction(self, direction):  # after 'time' delay and if
        if self.draw and self.exist and self.count == 20:  # Rocket exists
            self.direction = direction

    # Makes Rocket move if 'time' delay is over and Rocket exists
    def update(self):
        if self.draw and self.count == 20:
            self.rocket_moves[self.direction]()

    # Increases self.count if 'time' delay isn't over and Rocket exists
    def update_count(self):
        if self.count < 20 and self.draw:
            self.count += 1

    # Setting first coordinates
    def set_init_coor(self, hunter):
        if self.first:
            self.x = self.hunter.x
            self.y = self.hunter.y
            self.first = False

    @property
    def coordinate(self):
        return self.x, self.y

    @coordinate.setter
    def coordinate(self, xy: tuple):
        self.x, self.y = xy[0], xy[1]
