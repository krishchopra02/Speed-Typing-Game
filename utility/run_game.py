from utility.game_functions import display_text,load_target_text
import time
def run_game(stdscr):
    target_text = load_target_text()
    current_text = []
    wpm =0 
    start_time = time.time() 
    stdscr.nodelay(True)

    while True: 
        time_taken = max(time.time()-start_time,1)
        wpm = round((len(current_text)/(time_taken/60))/5)
        stdscr.erase()
        display_text(stdscr,target_text,current_text,wpm)

        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try: 
            key = stdscr.getkey()
        except :
            continue

        if ord(key) == 27:
            break 

        if key in ("KEY_BACKSPACE",'\b','\x7f'):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text) <len(target_text):
            current_text.append(key)
        
