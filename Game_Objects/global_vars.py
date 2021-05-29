from numpy import array

WIDTH = 45  # main screen's width
HEIGHT = 23  # main screen's height
MAX_X = WIDTH - 2  # max Ox coordinate for game objects
MAX_Y = HEIGHT - 2  # max Oy coordinate forgame objects
SNAKE_LENGTH = 3  # Snake's initial body length (without head)
SNAKE_X = SNAKE_LENGTH + 1  # Snake's head initial Ox coordinate
SNAKE_Y = 11  # Snake's head initial Oy coordinate
SPEED = 120  # initial game speed
CONT = False  # for 'TRY AGAIN' menu
NAME = ''  # ME
SHOT = False  # checking if Snake was shot by Hunter's rocket
HUNTER_PERIOD = 2

# ME AND THE BOYS (standart TOP PLAYERS)
TOP_PLAYERS = {'Chuck Norris': 9999,
               'xX_VovaPu_Xx': 101,
               'Doc Brown': 88,
               '¯\_(ツ)_/¯': 61,
               'Snake Plissken': 49,
               'Spider_Man1994': 30,
               'Hendrix': 27,
               'Anarki': 15,
               'sub_zer0': -1}

OX = array([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,  # left main wall
            34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34,  # right main wall
            1, 1, 2, 43, 43, 42,  # upper wall
            10, 11, 14, 29, 32, 33, 21, 22,  # mid wall
            6, 7, 8, 9, 10, 33, 34, 35, 36, 37])  # bottom wall
OY = array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,  # left main wall
            5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,  # right main wall
            2, 1, 1, 2, 1, 1,  # upper wall
            11, 11, 11, 11, 11, 11, 11, 11,  # mid wall
            21, 21, 21, 21, 21, 21, 21, 21, 21, 21])  # bottom wall

AMOUNT = len(OX)  # of spikes in the window
