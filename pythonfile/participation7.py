# animate a car as it drives across the screen, using curses

import time
import curses

COLS = 80
STARTROW = 10

DELAY = 0.25

# note space on LHS of each string to make it self-erasing
CAR = [
	'     ___     ',
	' ---/  |\____',
	' |_O______O_C',
]

# init curses
stdscr = curses.initscr()

# move the car across the screen horizontally
for startcol in range(COLS - len(CAR[0])):
	# draw the lines of the car
	for row in range(len(CAR)):
		stdscr.addstr(STARTROW+row, startcol, CAR[row])

	# wait for next animation step
	stdscr.refresh()
	time.sleep(DELAY)

curses.endwin()

