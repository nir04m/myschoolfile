import curses
import config
screen=curses.initscr()
curses.noecho()
player = '@'

# arranging the map

map = []
for i in range(24):
	map.append(['.']*80)


list=config.CONFIG.split('\n')

#READING THE MAP FROM CONFIG
for x in range(len(list)-1):
	line = list[x]
	if not line.strip():
		continue
	elif line[0] == 'R':
		RoomLine = line.split(' ')
		RoomXPos = int(RoomLine[1])
		RoomYPos = int(RoomLine[2])
		RoomWidth = int(RoomLine[3])
		RoomHeight = int(RoomLine[4])
	
		for i in range(RoomHeight):
			for j in range(RoomWidth):
				map[RoomYPos][RoomXPos] = ' '
				RoomXPos += 1
			RoomXPos -= RoomWidth
			RoomYPos += 1
		RoomYPos -= RoomHeight
	elif line[0] == 'c':
		RoomLine = line.split(' ')
		charletter = RoomLine[1]
		charXPos = int(RoomLine[2])
		charYpos = int(RoomLine[3])
		
		map[charYpos][charXPos] = charletter
	else:
		continue 


# PRINTING THE MAP
for j in range(24):
	for k in range(80):
		screen.move(j, k)
		screen.insch(map[j][k])

	# main user input loop
while True:
	# update (centered) label line
	screen.move(21, 0)
	screen.deleteln()			# new label may be shorter
	label = map[RoomYPos][RoomXPos]
	screen.addstr(2, (80 - len(label)) // 2, label)

	# update player and refresh (getkey should force refresh in any case)
	screen.addch(9,9,player)
	screen.refresh()

	# get input key
	ch = screen.getkey()

	if ch == 'j' or ch == 'a':
		if RoomXPos > 0 and map[RoomYPos][RoomXPos-1] != '.':
			screen.addch(RoomYPos,RoomXPos , player)	# restore char
			RoomXPos = RoomXPos - 1
			player = screen.inch(RoomYPos, RoomXPos)
	elif ch == 'l' or ch == 'd':
		if RoomXPos < 80-1 and map[RoomYPos][RoomXPos+1] != '.':
			screen.addch(RoomYPos,RoomXPos , player)	# restore char
			RoomXPos = RoomXPos + 1
			player = screen.inch(RoomYPos, RoomXPos)
	elif ch == 'w' or ch == 'i':
		if RoomYPos > 0 and map[RoomYPos-1][RoomXPos] != '.':
			screen.addch(RoomYPos,RoomXPos , player)	# restore char
			RoomYPos = RoomYPos - 1
			player = screen.inch(RoomYPos, RoomXPos)
	elif ch == 's' or ch == 'k':
		if RoomYPos < 24-1 and map[RoomYPos+1][RoomXPos] != '.':
			screen.addch(RoomYPos, RoomXPos , player)	# restore char
			RoomYPos = RoomYPos + 1
			player = screen.inch(RoomYPos, RoomXPos )




	if ch == 'q':
		break
curses.endwin()
