import turtle
n=42
sides=10
npoly=10
turtle.speed(1)
for j in range(3):
	for i in range(5):
		for k in range(10):
			turtle.fd(n)
			turtle.lt(360/sides)
		turtle.lt(180/5)
	turtle.lt(180/5) 

input()
turtle.done()
