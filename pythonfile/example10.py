# moving boxes, added in response to mouse click

import engine

WIDTH = 640
HEIGHT = 480
x = 0
y = 0

class Box(engine.GameObject):
	def __init__(self):
		super().__init__(x, y, +1, 0, 'square', 'red')

def mouse_cb(x, y):
	box = Box(x,y)
	engine.add_obj(box)
	print('Mouse click at', x, y)

if __name__ == '__main__':
	engine.init_screen(WIDTH, HEIGHT)
	engine.init_engine()
	engine.set_mouse_handler(mouse_cb)
	engine.engine()

