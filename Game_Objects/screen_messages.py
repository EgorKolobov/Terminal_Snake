import curses


def wasted_screen(window):  # Wasted
    window.addstr(
        7, 5, '                   _           _', curses.color_pair(1))
    window.addstr(
        8, 5, '                  | |         | |', curses.color_pair(1))
    window.addstr(
        9, 5, '__      ____ _ ___| |_ ___  __| |', curses.color_pair(1))
    window.addstr(
        10, 5, '\ \ /\ / / _  / __| __/ _ \/ _  |', curses.color_pair(1))
    window.addstr(
        11, 5, ' \ V  V / (_| \__ \ ||  __/ (_| |', curses.color_pair(1))
    window.addstr(
        12, 5, '  \_/\_/ \__,_|___/\__\___|\__,_|', curses.color_pair(1))


def game_over_screen(window):  # Game Over
    window.addstr(
        2, 3,  '/$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$', curses.color_pair(1))
    window.addstr(
        3, 2, '/$$__  $$ /$$__  $$| $$$    /$$$| $$_____/', curses.color_pair(1))
    window.addstr(
        4, 1, '| $$  \__/| $$  \ $$| $$$$  /$$$$| $$', curses.color_pair(1))
    window.addstr(
        5, 1, '| $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$', curses.color_pair(1))
    window.addstr(
        6, 1, '| $$|_  $$| $$__  $$| $$  $$$| $$| $$__/', curses.color_pair(1))
    window.addstr(
        7, 1, '| $$  \ $$| $$  | $$| $$\  $ | $$| $$', curses.color_pair(1))
    window.addstr(
        8, 1, '|  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$', curses.color_pair(1))
    window.addstr(
        9, 2, '\______/ |__/  |__/|__/     |__/|________/', curses.color_pair(1))
    window.addstr(
        11, 3,  '/$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$', curses.color_pair(1))
    window.addstr(
        12, 2, '/$$__  $$| $$   | $$| $$_____/| $$__  $$', curses.color_pair(1))
    window.addstr(
        13, 1, '| $$  \ $$| $$   | $$| $$      | $$  \ $$', curses.color_pair(1))
    window.addstr(
        14, 1, '| $$  | $$|  $$ / $$/| $$$$$   | $$$$$$$/', curses.color_pair(1))
    window.addstr(
        15, 1, '| $$  | $$ \  $$ $$/ | $$__/   | $$__  $$', curses.color_pair(1))
    window.addstr(
        16, 1, '| $$  | $$  \  $$$/  | $$      | $$  \ $$', curses.color_pair(1))
    window.addstr(
        17, 1, '|  $$$$$$/   \  $/   | $$$$$$$$| $$  | $$', curses.color_pair(1))
    window.addstr(
        18, 2, '\______/     \_/    |________/|__/  |__/', curses.color_pair(1))


def logo_screen(table):  # Terminal Snake
    table.addstr(1, 1, '___ __  __  .  . ___ .  .  __  .',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(2, 1, ' | |__ |__| |\/|  |  |\ | |__| |',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(3, 1, ' | |__ |  \ |  | _|_ | \| |  | |_',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(5, 2, 'SSSSS N   N   AAA   K  K  EEEEE',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(6, 2, 'S     NN  N  A   A  K K   E',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(7, 2, 'SSSSS N N N AAAAAAA KKK   EEEEE',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(8, 2, '    S N  NN A     A X  K  E',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(9, 2, 'SSSSS N   N A     A X  KK EEEEE',
                 curses.color_pair(5) + curses.A_BOLD)
    table.addstr(10, 33, '™')
