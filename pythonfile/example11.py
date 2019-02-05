#imports the game.object for the game
import time
import random
import engine
import turtle
import math

WIDTH = 640
HEIGHT = 480
MAXY = HEIGHT // 2
MINY = -HEIGHT // 2
MAXX = WIDTH // 2
MINX = -WIDTH // 2
TEXTCOLOR = 'black'
MYX = 0
MYY = -108
MYDELTA = 0
MYMAXMOVE = 0
MYCOLOR = 'blue'
MYSHAPE = 'square'

#parameters for objects
Holeshape = 'circle'
Holescolor = 'black'
groundfire = 0
GROUNDY = MINY + HEIGHT // 4
NEWENEMYPROB = 0.01
DEMOFIREPROB = 0.01
XFALLRATE = 1
YFALLRATE = -2
THEMCOLOR = 'purple'
USCOLOR = 'red'
CITYCOLORS = ('green', 'yellow', 'red')
CITYLIVES = len(CITYCOLORS)
EXPLODECOLOR = 'orange'
BGCOLOR = 'black'
GROUNDCOLOR = 'orange'
NCITIES = 6
GUNX = 0
GUNY = GROUNDY
CLIMBRATE = 3 * XFALLRATE
NSTARS = 25
countofmissilex = 0
countofmissiley = 0
gameover = False

class S:
	def __init__(self):
		self.playing = False
		self.me = None
		self.score = 0
		
s = None

class Replay(BaseException):
	pass



class Me(engine.GameObject):
	def __init__(self):
		super().__init__(MYX,MYY,0,MYDELTA,MYSHAPE,MYCOLOR)
		self.uptime = -1
	def delete(self):
		super().delete()
		
	
	def flap(self):
		self.deltay = +2
		self.uptime = 35

	def move(self):
		self.uptime -= 1
		if self.uptime < 0 and self.y >-110:
			self.deltay = -2
		elif self.uptime < 0 and self.y ==-110:
			self.deltay = 0
		global injump
		global groundfire
		if self.deltay != 0:
			injump = True
		else:
			injump = False
		super().move()

	def getx(self):		return self.x
	def gety(self):		return self.y
	
	def get_bc(self):
		# bounding circle, for circle-based collision detection
		return self.x, self.y, 20


class Ground(engine.GameObject):
	def __init__(self, ulx, uly, lrx, lry):
		self.groundlevel = uly
		turtle.register_shape('ground', (
			(ulx, uly), (lrx, uly), (lrx, lry), (ulx, lry)
		))
		super().__init__(0, 0, 0, 1, 'ground', GROUNDCOLOR)

	def get_groundlevel(self):
		return self.groundlevel
	
	def isstatic(self):
		return True

class Boom(engine.GameObject):
	def __init__(self, x, y, maxdiameter):
		self.maxdiameter = maxdiameter
		self.diameter = 0
		super().__init__(x, y, 0, 0, 'circle', EXPLODECOLOR)

	def draw(self):
		oldmode = turtle.resizemode()
		turtle.shapesize(outline=self.diameter)
		id = super().draw()
		turtle.resizemode(oldmode)
		return id
	
	def get_bc(self):
		# bounding circle, for circle-based collision detection
		return self.x, self.y, self.diameter

	def step(self):
		newsize = abs(math.sin(math.radians(self.age) + 180))
		if newsize < 0.05:
			engine.del_obj(self)
			return
		self.diameter = newsize * (self.maxdiameter * 2)
		super().step()



class Holes(engine.GameObject):
	def __init__(self, x, y, deltax, deltay):
		super().__init__(250,-120,-1,0,'circle','black')
		
	def get_bc(self):
		# bounding circle, for circle-based collision detection
		return self.x, self.y, 10
	

class Rocks(engine.GameObject):
	def __init__(self, x, y, deltax, deltay):
		super().__init__(250,-108,-1,0,'turtle','green')
		
	def get_bc(self):
		# bounding circle, for circle-based collision detection
		return self.x, self.y, 10
	
def hitenemy():
	global score
	score = score + 10	
	draw_score()
	
def Holes_cb():
	obj = Holes(random.randint(0,1), 0,-0, -1)
	engine.add_obj(obj)

def Rocks_cb():
	obj = Rocks(random.randint(0,1), 0,-0, -1)
	engine.add_obj(obj)

class missileside(engine.GameObject):
	def __init__(self,x,y,deltax,deltay):
		super().__init__(MYX,MYY,+2,0,'triangle','yellow')
	def get_bc(self):
		# bounding circle, for circle-based collision detection
		return self.x, self.y, 10
	def delete(self):
		global countofmissilex
		countofmissilex =  countofmissilex -1
		super().delete()
		
class missileup(engine.GameObject):
	def __init__(self,x,y,deltax,deltay):
		super().__init__(MYX,MYY,0,+2,'triangle','yellow')
	def get_bc(self):
		# bounding circle, for circle-based collision detection
		return self.x, self.y, 10
	def delete(self):
		global countofmissiley
		countofmissiley =  countofmissiley -1
		super().delete()

def upmissile_cb():
	obj = missileup(0,0,0,+1)
	engine.add_obj(obj)

def sidemissile_cb():
	obj = missileside(0,0,0,+1)
	engine.add_obj(obj)


#keyboard input to play the game
def input_cb(key):
	global countofmissilex
	global countofmissiley
	if key == 'q' or key == 'Q':
		exit()
	if key == 'space' and injump == False:
		s.me.flap()
	if key == 'Return' and gameover == False and countofmissilex < 4 and countofmissiley < 4 and injump == False:
		countofmissilex = countofmissilex + 1
		countofmissiley = countofmissiley + 1
		upmissile_cb()
		sidemissile_cb()
# collision detection
def iscoll_circle(obj1, obj2):
	x1, y1, r1 = obj1.get_bc()
	x2, y2, r2 = obj2.get_bc()
	
	# from http://devmag.org.za/2009/04/13/basic-collision-detection-in-2d-part-1/
	# take the Euclidean distance between the center points, and if
	# that's less than the sum of the radii, then intersection occurred
	d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	return d < (r1 + r2)

def coll_Me(obj1, obj2):
	if iscoll_circle(obj1, obj2):
		x1, y1, r1 = obj1.get_bc()
		x2, y2, r2 = obj2.get_bc()
		engine.add_obj(Boom(x1, y1, r1))
		engine.add_obj(Boom(x2, y2, r2))
		engine.del_obj(obj1)
		
		endgame()
		
def coll_Me2(obj1, obj2):
	if iscoll_circle(obj1, obj2):
		x1, y1, r1 = obj1.get_bc()
		x2, y2, r2 = obj2.get_bc()
		engine.add_obj(Boom(x1, y1, r1))
		engine.add_obj(Boom(x2, y2, r2))
		
		engine.del_obj(obj2)
		endgame()
	
		
def coll_missile(obj1, obj2):
	if iscoll_circle(obj1, obj2):
		x1, y1, r1 = obj1.get_bc()
		x2, y2, r2 = obj2.get_bc()
		engine.add_obj(Boom(x1, y1, r1))
		engine.add_obj(Boom(x2, y2, r2))
		engine.del_obj(obj1)
		engine.del_obj(obj2)
		hitenemy()
#title screen display
def banner(s,color = TEXTCOLOR):
	turtle.home()
	turtle.color(color)
	turtle.write(s, True, align='center', font=('Arial',48, 'italic'))
	time.sleep(3)
	turtle.undo()
	
def title_screen():
	banner('TURTLE\nBUGGY')
# star display in the game
def draw_stars():
	for i in range(NSTARS):
		x = random.randint(MINX, MAXX)
		y = random.randint(GROUNDY, MAXY)
		turtle.goto(x, y)
		turtle.color('white')
		turtle.dot(1)
# displays score in the game
def draw_score():
	turtle.goto(0, GROUNDY-25)
	turtle.dot(50, GROUNDCOLOR)
	turtle.color('black')
	turtle.write(score, align='center', font=('Arial', 14, 'normal'))
#gameover function 
def endgame():
	turtle.goto(0, GROUNDY-50)
	turtle.dot(50, GROUNDCOLOR)
	turtle.color('black')
	turtle.write('gameover', align='center', font=('Arial', 14, 'normal'))
	global gameover
	gameover = True

def play(postfn=None):
	global s,score
	s = S()
	score = 0
	engine.add_obj(Ground(MINX, GROUNDY, MAXX, MINY))
	engine.add_random_event(0.002, Holes_cb)
	engine.add_random_event(0.007, Rocks_cb)
	engine.register_collision(Me, Holes, coll_Me)
	engine.register_collision(Holes, Me, coll_Me2)
	engine.register_collision(Me, Rocks, coll_Me)
	engine.register_collision(Rocks, Me, coll_Me2)
	engine.register_collision(Me, Rocks, coll_Me)
	engine.register_collision(Rocks, Me, coll_Me)
	engine.register_collision(missileside, Rocks, coll_missile)
	engine.register_collision(Rocks, missileside, coll_missile)

	draw_stars()
	draw_score()
	s.me = Me()
	engine.add_obj(s.me)


	s.playing = True
	if postfn:
		postfn()
	engine.engine()


def game():
	engine.init_engine()
	engine.set_keyboard_handler(input_cb)
	play()	

if  __name__ == '__main__':
	#title_screen()
	engine.init_screen(WIDTH, HEIGHT)
	turtle.bgcolor(BGCOLOR)
	turtle.tracer(1000)
	#banner('Get ready...')
	game()
