import curses
from curses import wrapper
from utility.run_game import run_game
from utility.game_functions import initialize_game

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

    initialize_game(stdscr)
    while True:
        run_game(stdscr)
        stdscr.addstr(2,0,"The results of your test are above! Press any key to continue and escape key to stop...")
        key = stdscr.getkey()

        if ord(key)== 27:
            break;
wrapper(main)