# rpn calculator
# one command per line, end with "end"
# numbers in input assumed all positive integers
# stack used for evaluation: append() "pushes" onto end, pop() "pops" off end

stack = []

while True:
	line = input('? ')

	if line == 'end':
		break

	elif line == '+':
		if len(stack) < 2:
			print('error: not enough arguments')
			continue
		a = stack.pop()
		b = stack.pop()
		stack.append(a + b)

	elif line == '-':
		if len(stack) < 2:
			print('error: not enough arguments')
			continue
		a = stack.pop()
		b = stack.pop()
		stack.append(a-b)
	
		
	elif line == '*':
		if len(stack) < 2:
			print('error: not enough arguments')
			continue
		a = stack.pop()
		b = stack.pop()
		stack.append(a * b)

	elif line == 'print':
		if len(stack) < 1:
			print('error: nothing to print')
			continue
		print('=', stack.pop())

	elif line.isdigit():			# a good thing to look up
		stack.append(int(line))

	else:
		print('error: I have no clue what this is')
