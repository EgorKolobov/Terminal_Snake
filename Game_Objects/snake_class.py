import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

# ==============================================================================
# Snake. Can move only up, down, right or left. Likes apples.
WIDTH = 45  # main screen's width
HEIGHT = 23  # main screen's height
MAX_X = WIDTH - 2  # max Ox coordinate for game objects
MAX_Y = HEIGHT - 2  # max Oy coordinate forgame objects


class Snake():

    dont_move = {  # doesn't allow Player to move in opposite direction
        KEY_UP: KEY_DOWN,
        KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT,
        KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, len, speed, window):
        self.body_parts = []
        self.points = 0  # Snake's points(Score)
        self.speed = speed
        self.len = len

        for i in range(self.len, 0, -1):  # adding all body parts(no head)
            self.body_parts.append(Body(x - i, y))
        # adding head(and choosing its character)
        self.body_parts.append(Body(x, y, '▣'))
        self.window = window  # choosing main window
        self.direction = KEY_RIGHT  # Snake's initial direction
        self.last_head_coordinate = (x, y)  # last head coordinates (obvious)
        self.direction_moves = {  # making a dictionary of Snake's moves
            KEY_UP: self.go_up,
            KEY_DOWN: self.go_down,
            KEY_LEFT: self.go_left,
            KEY_RIGHT: self.go_right
        }

    # Snake's head (just for convinience)
    @property
    def head(self):
        return self.body_parts[-1]  # last elemaent in list==head

    # Show Snake's points(Score) string on the screen (window)
    @property
    def score(self):
        return ' Score : {} '.format(self.points)

    # Eating food. The one of the most important functions
    def eat_food(self, food):
        food.reset()  # giving to a Food obj new coordinates (see line 191)
        # making a local Body obj
        body = Body(self.last_head_coordinate[0], self.last_head_coordinate[1])
        self.body_parts.insert(-1, body)  # adding a new body part
        self.points += 1  # increasing Snake's points
        if self.points % 5 == 0 and self.speed > 65:  # speed limit
            self.speed -= 22  # speed increasement every 5 points
            self.window.timeout(self.speed)
        curses.beep()  # beep signal after eeating food

    # Used in 'injured', 'crashed', 'shot' functions
    @property  # (it's just convinient)
    def coordinate(self):
        return self.head.x, self.head.y

    # Returns True if Snake was injured by spikes.
    def injured(self, spikes):  # if Snake's head==any spike return True
        return any([spike.coordinate == self.head.coordinate and spike.exist
                    for spike in spikes.obstacles])

    # Returns True if Snake bited itself.
    @property
    def crashed(self):  # if Snake's head==any body part return True
        return any([body.coordinate == self.head.coordinate
                    for body in self.body_parts[:-1]])

    # Returns True if Snake has been killed by a Hunter.
    def shot(self, rckt):  # if any Snake's body part r head==Rocket part return True
        return any([body.coordinate == rckt.coordinate
                    for body in self.body_parts])

    # Makes body follows Snake's head + moves Snake
    def update(self):
        last_body = self.body_parts.pop(0)
        last_body.x = self.head.x
        last_body.y = self.head.y
        self.body_parts.insert(-1, last_body)
        self.last_head_coordinate = (self.head.x, self.head.y)
        self.direction_moves[self.direction]()

    # Set a new direction for Snake.
    def change_direction(self, direction):
        if direction != Snake.dont_move[self.direction]:
            self.direction = direction

    # Render Snake
    def render(self):
        for body in self.body_parts:
            self.window.addstr(body.y, body.x, body.char, curses.color_pair(2))

    def go_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y

    def go_down(self):
        self.head.y += 1
        if self.head.y > MAX_Y:
            self.head.y = 1

    def go_left(self):
        self.head.x -= 1
        if self.head.x < 1:
            self.head.x = MAX_X

    def go_right(self):
        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1

# ==============================================================================
# A part of Snake's body(tail)


class Body():
    def __init__(self, x, y, char='O'):
        self.x = x
        self.y = y
        self.char = char  # represents Body obj on the screen

    @property
    def coordinate(self):
        return self.x, self.y
