import curses
from Game_Objects.global_vars import MAX_X, MAX_Y

'''
Hunter. Follows an appropriate route and shoots rockets(up or down)
Appears every 15 points in upper left corner.
Very dangerous enemy. The only way to get rid of him is to eat him or make him crash
'''


class Hunter():  # make him bump into Snake's Tail.
    def __init__(self, window, char="H"):
        self.window = window
        self.x = -1  # see commets in lines 207-209
        self.y = -1
        self.exist = False  # allow to exist
        self.char = char  # character that represents Hunter onthe screen
        self.direction = 'RIGHT'  # initial direction

        self.hunter_moves = {  # making a dictionary of Hunter's moves
            'UP': self.go_up,
            'DOWN': self.go_down,
            'LEFT': self.go_left,
            'RIGHT': self.go_right
        }

    def go_up(self):
        self.y -= 1
        if self.y < 1:
            self.y = MAX_Y

    def go_down(self):
        self.y += 1
        if self.y > MAX_Y:
            self.y = 1

    def go_left(self):
        self.x -= 1
        if self.x < 1:
            self.x = MAX_X

    def go_right(self):
        self.x += 1
        if self.x > MAX_X:
            self.x = 1

    # Renders Hunter in the screen if it exists
    def render(self):
        if self.exist:
            self.window.addstr(self.y, self.x, self.char, curses.A_BOLD)

    # makes Hunter moveit it exists
    def update(self):
        if self.exist:
            self.hunter_moves[self.direction]()

    # Used in destroying Hunter(see line 623)
    @property
    def coordinate(self):
        return self.x, self.y

    @coordinate.setter
    def coordinate(self, xy: tuple):
        self.x, self.y = xy[0], xy[1]

    # Hunter's route. It wil follow this route untill
    def route(self):  # destroyed or changed with another Hunter
        if self.exist:
            if self.x == 3 and self.y == 2:
                self.direction = 'RIGHT'
            elif self.x == 40 and self.y == 2:
                self.direction = 'DOWN'
            elif self.x == 40 and self.y == 20:
                self.direction = 'LEFT'
            elif self.x == 3 and self.y == 20:
                self.direction = 'UP'
