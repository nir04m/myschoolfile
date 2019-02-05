def f(n):
	if n < 5:
		return n - 2
	return n - f(n - 1)
	
	
f(-3)