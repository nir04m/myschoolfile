# moving boxes, added in response to space bar being pressed
import random
import engine

WIDTH = 640
HEIGHT = 480

class S:
	def __init__(self):
		self.playing = False	# game state
		self.me = None
		self.score = 0
		self.pipecounter = 0
s = None


class Box(engine.GameObject):
	def __init__(self):
		super().__init__(0, 0, +1, 0, 'square', 'red')

def newpipe_cb():
	s.pipecounter -= 1
	if s.pipecounter <= 0:
		s.pipecounter = PIPEFREQ
		lheight = random.randint(PIPEMIN, PIPEUNITS-PIPEGAP-PIPEMIN)
		uheight = PIPEUNITS-lheight-PIPEGAP
		l = lowerpipe(ht2name(lheight), lheight*PIPEUNIT)
		u = upperpipe(ht2name(uheight), uheight*PIPEUNIT)
		engine.add_obj(l)
		engine.add_obj(u)

if __name__ == '__main__':
	s = S()
	engine.init_screen(WIDTH, HEIGHT)
	engine.init_engine()
	engine.add_random_event(1.0, newpipe_cb)
	
	engine.engine()

