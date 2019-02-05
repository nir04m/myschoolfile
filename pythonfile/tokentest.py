import token
import tokenize

# Returns a list of (token, attribute) tuples corresponding to the
# tokens in the input Python 3 filename passed as a parameter.  Assumes
# that the file actually does contain valid Python code.  Returns None
# in the event of any error.

def file2tokens(filename):
	try:
		f = open(filename, 'rb')
		tokens = []
		for t in tokenize.tokenize(f.readline):
			tokens.append( (token.tok_name[t.type], t.string) )
		f.close()
	except IOError:
		return None
	return tokens

if __name__ == '__main__':
	import sys
	for filename in sys.argv[1:]:
		print(file2tokens(filename))
