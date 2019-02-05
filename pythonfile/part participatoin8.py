# rpn calculator
# one command per line, end with "end"
# numbers in input assumed all positive integers
# stack used for evaluation: append() "pushes" onto end, pop() "pops" off end

# reflection version

stack = []

def cmd_end():
	# XXX stuff goes here

def cmd_add():
	if len(stack) < 2:
		print('error: not enough arguments')
		return
	a = stack.pop()
	b = stack.pop()
	stack.append(a + b)

def cmd_mul():
	if len(stack) < 2:
		print('error: not enough arguments')
		return
	a = stack.pop()
	b = stack.pop()
	stack.append(a * b)

def cmd_print():
	if len(stack) < 1:
		print('error: nothing to print')
		return
	print('=', stack.pop())

while True:
	line = input('? ')

	if line.isdigit():			# a good thing to look up
		stack.append(int(line))
	else:
		# XXX stuff goes here
		else:
			print('error: I have no clue what this is')
