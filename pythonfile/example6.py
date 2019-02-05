import sys

# Returns a list of lines that the text file specified by the filename
# contains, or None if there was some problem.

def readlines(filename):
	try:
		f = open(filename, 'r')
		rv = f.readlines()
		f.close()
	except IOError:
		rv = None
	return rv

#takes a list of lines and print ransom text

def ransom(L):
	for lines in L:
		newline = ""
		for ch in lines:
			if ch.isalpha():
				if random.randint(0,1) == 0:
					ch = ch.upper()
				else:
					ch = ch.lower()
			newline = newline +ch
		print(newline,end='')



# Check for command line argument,print usage message if no argument present
if len(sys.argv) != 2:
	print("Usage: python3",sys.argv [0],"filename")

# Use readlines function to get a list of lines from input file
lines = readlines(sys.srgv[1])
if lines == None:
	print('Error reading file')
	sys.exit()
# Call ransom function using the list of lines 
ransom(lines)