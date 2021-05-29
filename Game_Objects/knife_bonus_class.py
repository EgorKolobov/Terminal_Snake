from Game_Objects.collectable_class import *

'''
Knife Bonus. Cuts off 4 Snake's body parts, but doesn't affect the Score.
Appears randomly(chance == 0.45) after round 5 and if Snake length>8
Dissappeares after a short period of time
'''


class Knife_Bonus(Collectable):
    def __init__(self, window, char: chr = '@', color_pair: int = 3):
        super().__init__(window, char, color_pair)
        self.count = 0  # a 'time'(counts frames)delay variable. If it reaches 160,
        self.exist = False  # Doesn't allow to render Knife Bonus.

    # Renders Knife Bonus if it exists & 'time' delay is over
    def render(self):
        if self.exist and self.count < 161:
            self.window.addstr(self.y, self.x, self.char,
                               curses.color_pair(3) + curses.A_BLINK)
            self.count += 1  # self.count+=1 every frame(the simpliest delay)

    # Sets a new coordinates if Knife Bonus exists
    def reset(self):
        if self.exist:
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
            self.count = 0
