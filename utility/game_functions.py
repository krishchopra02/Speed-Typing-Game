import random
import curses

def initialize_game(stdscr):
    stdscr.erase()
    stdscr.addstr("Speed Typing Game")
    stdscr.addstr("\n Press any key to get started")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr,target,user_input,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"Words Per Minute: {wpm}")

    for i,entered_char in enumerate(user_input):
        correct_char=target[i]
        color = curses.color_pair(1)
        if entered_char !=correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0,i,entered_char,color)
    
def load_target_text():
    with open("target_text.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip() #To remove any empty spaces before or after


