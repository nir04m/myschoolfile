import difflib

# Returns a float indicating how closely matched the two sequences
# passed in as arguments are.  A result >= 0.6 should be a close match.

def similarity(L1, L2):
	matcher = difflib.SequenceMatcher(None, L1, L2)
	return matcher.ratio()

if __name__ == '__main__':
	print(similarity(
		['a', 'b'],
		['a', 'b', 'c']
	))
	print(similarity(
		['a', 'b'],
		['b', 'a']
	))
	print(similarity(
		['a', 'b'],
		['a', 'c', 'b']
	))
	print(similarity(
		range(10),
		range(2, 12)
	))
	print(similarity(
		range(10),
		range(6, 12)
	))
		
