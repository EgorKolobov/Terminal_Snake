import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint, random
import time
# custom classes Game_Objects
from Game_Objects.global_vars import *
from Game_Objects.snake_class import Snake
from Game_Objects.food_class import Food
from Game_Objects.snail_bonus_class import Snail_Bonus
from Game_Objects.knife_bonus_class import Knife_Bonus
from Game_Objects.obstacle_array_class import ObstacleArray
from Game_Objects.hunter_class import Hunter
from Game_Objects.rocket_class import Rocket
from Game_Objects.screen_messages import wasted_screen, game_over_screen, logo_screen


def ask_name(wind):
    global NAME  # Player's name
    while True:
        letter = wind.getch()
        if letter == 10:
            break
        elif 0 <= letter <= 256 and letter != 127 and letter != 22:
            NAME += chr(letter)
        elif letter == 127 or letter == 22:
            NAME = NAME[:-1]
        wind.addstr(11, 10, ' NAME : {} '.format(NAME, curses.color_pair(6)))


# Starting main game file
if __name__ == '__main__':

    curses.initscr()
    # INITIALIZING COLOR PAIRS =================================================
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # apples
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # snake
    curses.init_pair(3, curses.COLOR_BLUE,
                     curses.COLOR_BLACK)  # knife+TRY AGAIN
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # snail
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Score+HINT
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)  # messages
    # ===== ININTIALIZING MAIN WINDOW ==========================================
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(SPEED)
    window.keypad(True)  # enables KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
    curses.noecho()  # turns off automatic echoing of keys to the screen
    window.border(0)  # draws border
    window.addstr(10, 10, 'Enter your name, gamer.', curses.color_pair(3))
    ask_name(window)  # asking name
    # ===== MAKING HINT WINDOW =================================================
    hint = curses.newwin(HEIGHT - 15, 35, HEIGHT - 8, 45)
    hint.border(0)
    hint.addstr(0, 8, ' HINT : ', curses.color_pair(5))

    hint.addstr(1, 1, "◉", curses.color_pair(1))
    hint.addstr(1, 2, " -apple. Eat it to gain points.", curses.color_pair(6))

    hint.addstr(2, 1, "✕")
    hint.addstr(2, 2, " -spike. Damages the Snake.", curses.color_pair(6))

    hint.addstr(3, 1, "@", curses.color_pair(4))
    hint.addstr(3, 2, " -snail. Slows down the Snake.", curses.color_pair(6))

    hint.addstr(4, 1, "%", curses.color_pair(3))
    hint.addstr(4, 2, " -knife. Shortens the Snake.", curses.color_pair(6))

    hint.addstr(5, 1, "H", curses.A_BOLD)
    hint.addstr(5, 3, "-hunter. Shoots rockets.", curses.color_pair(6))

    hint.addstr(6, 1, "◈", curses.A_BOLD)
    hint.addstr(6, 2, " -rocket. Delivers pain.", curses.color_pair(6))
    hint.refresh()
    # ===== TERMINAL SNAKE window +TOP PLAYERS table ===========================
    table = curses.newwin(HEIGHT - 8, 35, 0, 45)
    # ===== MAIN GAME LOOP =====================================================
    while True:

        window.clear()  # deleting everything from window (game screen)
        window.border(0)  # drawing border in window
        if not CONT:
            table.clear()  # deleting everithing from table (game logo screen)
            table.border(0)  # drawing border in table
            logo_screen(table)
            table.refresh()
        curses.curs_set(0)
        curses.noecho()

        for i in range(3, 0, -1):
            timer = 'GAME STARTS IN: {}'.format(i)
            window.addstr(10, 10, timer, curses.color_pair(3))
            window.refresh()
            time.sleep(1)
        # ===== GAME OBJECTS ===================================================
        python = Snake(SNAKE_X, SNAKE_Y, SNAKE_LENGTH, SPEED, window)  # making Snake
        # setting speed(in case if Player tries to play again)
        python.speed = SPEED
        apple = Food(window, '◉')  # making Food
        snail = Snail_Bonus(window, '@')  # making Snail Bonus
        knife = Knife_Bonus(window, '%')  # Knife Bonus
        predator = Hunter(window, 'H')  # making Hunter
        rckt = Rocket(window, predator, '◈')  # making Rocket
        spikes = ObstacleArray(window)
        # ===== ACTUAL GAME LOOP ===============================================
        while True:
            window.clear()  # clearing window for a new game
            window.border(0)  # drawing borders
            window.addstr(0, 15, python.score, curses.color_pair(5))
            # Snake, apple and spikes rendering ----------------------------------------
            python.render()
            apple.render()
            spikes.render()
            snail.render()  # rendering Snail Bonus
            knife.render()  # rendering Knife Bonus
            # ------------------------------------------------------------------
            # Hunter & rocket rendering rules ----------------------------------
            predator.render()  # rendering Hunter
            predator.route()  # Hunter follows his route
            rckt.render()  # render Rocket
            # ------------------------------------------------------------------
            # rocket move rules (do not touch!) --------------------------------
            if predator.direction in {'UP', 'RIGHT'}:
                rckt.change_direction('DOWN')
            else:
                rckt.change_direction('UP')
            if rckt.y == MAX_Y - 1 or rckt.y == 1:
                rckt.exist = True
                rckt.y = predator.y
                rckt.x = predator.x
            else:
                rckt.exist = False
            # ------------------------------------------------------------------
            # checking if apple==spike
            if any(spike.coordinate == apple.coordinate and spike.exist for spike in spikes.obstacles):
                apple.reset()

            # checking if knife==spike
            if any(spike.coordinate == knife.coordinate and spike.exist for spike in spikes.obstacles):
                knife.reset()

            # checking if snail==spike
            if any(spike.coordinate == snail.coordinate and spike.exist for spike in spikes.obstacles):
                snail.reset()

            # moving Snake
            event = window.getch()
            if event in {KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT}:
                python.change_direction(event)

            # adjusting up/down speed-------------------------------------------
            if python.direction in {KEY_UP, KEY_DOWN}:
                window.timeout(python.speed+60)  # decreasing up & down speed
            if python.direction in {KEY_LEFT, KEY_RIGHT}:
                window.timeout(python.speed)  # restoring right & left speed
            # ------------------------------------------------------------------

            # eating apple (very important step)
            if python.head.coordinate == apple.coordinate:
                python.eat_food(apple)
                spikes.update()
                # setting Snail Bonus coordinates(every 5 points)
                if python.points % 5 == 0 and python.speed < 100:
                    snail.exist = True
                    snail.reset()
                # seting Knife Bonus coordinates
                if python.points > 5 and random() < 0.45 and len(python.body_parts) > 8:
                    knife.exist = True
                    knife.reset()
                # predator & rocket appearence settings
                if python.points % HUNTER_PERIOD == 0 and python.points != 0:
                    predator.exist = True
                    predator.x = 3
                    predator.y = 2
                    rckt.exist = True
                    rckt.draw = True
                    rckt.first = True
                    rckt.count = 0

            # eating Snail Bonus
            if python.head.coordinate == snail.coordinate:
                python.speed += 20
                snail.exist = False
                snail.y = -1  # hiding speed bonus

            # eating Knife Bonus
            if python.head.coordinate == knife.coordinate:
                del python.body_parts[:4]
                knife.exist = False
                knife.y = -1

            # destroying Hunter
            if any(body.coordinate == predator.coordinate for body in python.body_parts):
                curses.flash()
                predator.exist = False
                predator.y = -1
                predator.x = -1
                rckt.draw = False
                rckt.exist = False
                rckt.y = -1
                rckt.x = -1

            # if Snake got shot by rocket
            SHOT = python.shot(rckt)

            python.update()  # updating Snake
            predator.update()  # updating Hunter
            rckt.update_count()  # updating Rocket 'time' delay
            if rckt.count == 20:  # setting Rocket's initial coordinates
                rckt.set_init_coor(predator)
            rckt.update()  # updating Rocket

            # Snake dies :( ----------------------------------------------------
            if python.injured(spikes) or python.crashed or SHOT:
                time.sleep(2)
                window.clear()
                window.border(0)
                # GAME OVER menu
                if SHOT:  # if Snake got shot by rocket write 'WASTED'
                    wasted_screen(window)
                else:  # write 'GAME OVER'
                    game_over_screen(window)

                note = 'your current scrore is : {}'.format(python.points)
                window.addstr(20, 7, note, curses.color_pair(6))
                window.refresh()
                time.sleep(5)  # delay after 'GAME OVER' / 'WASTED'

                # adding player to TOP_PLAYERS
                if NAME not in TOP_PLAYERS.keys() or python.points > TOP_PLAYERS[NAME]:
                    TOP_PLAYERS[NAME] = python.points

                # sorting TOP_PLAYERS by value (by player's score)
                TOP_PLAYERS = dict(
                    sorted(TOP_PLAYERS.items(), key=lambda item: item[1], reverse=True))

                table.clear()
                table.border(0)
                table.refresh()
                table.addstr(0, 8, ' TOP PLAYERS : ', curses.color_pair(5))

                # drawing TOP_PLAYERS
                ind = 0
                for name, score in TOP_PLAYERS.items():
                    info = '[{}] {} : {}'.format(ind + 1, name, score)
                    if name == NAME:
                        table.addstr(2 + ind, 2, info, curses.A_BOLD)
                    else:
                        table.addstr(2 + ind, 2, info, curses.color_pair(6))
                    ind += 1
                table.refresh()

                time.sleep(2)
                break
        # ----------------------------------------------------------------------
        # TRY AGAIN menu -------------------------------------------------------
        window.clear()
        window.border(0)
        window.addstr(10, 11, 'TRY AGAIN?',
                      curses.color_pair(3) + curses.A_BOLD)
        window.addstr(11, 6, "press 'y' to restart or 'n' to quit",
                      curses.A_BLINK + curses.color_pair(6))
        note = 'your current scrore is : {}'.format(python.points)
        window.addstr(20, 7, note, curses.color_pair(6))
        window.refresh()
        # ----------------------------------------------------------------------
        # Responding to TRY AGAIN
        while True:
            ANS = window.getch()  # getting key's code
            if ANS == 121:  # 'y'
                CONT = True  # continue game
                break
            elif ANS == 110:  # 'n'
                CONT = False  # quit
                break

         # closing game
        if not CONT:
            break

    curses.endwin()  # setting terminal back to normal condition
