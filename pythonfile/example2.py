import difflib
import sys
D ={}

def imp(l2):
	for i in range(len(l2)):
		if l2[i][1] == 'import':
			if l2[i+1][1] == 'argv':
				continue		 
			list1 = l2[i+1][1]
			if list1 not  in D:
				D[list1] = 1
			else:
				D[list1] = D[list1] +1
			if D[list1] == 1:
				print(list1)
		if l2[i][1] == 'from':
			print(l2[i+1][1])

def dager(l3):
	f1 = []
	f2 = []
	for i in range(len(l3)):
		if l3[i][1] == 'import':
			f1.append(l3[i][1])
		elif l3[i][1] == 'eval':
			f1.append(l3[i][1])
		elif l3[i][1] == 'exec':
			f1.append(l3[i][1])
		elif l3[i][1] == 'open':
			fi.append(l3[i][1])
		elif l3[i][1][0:2] == '__' and l3[i][1][-2:] == '__':
			f1.append(l3[i][1])
	for listname in f1:
		if listname not in f2:
			f2.append(listname)
			print(listname, 'x', f1.count(listname))

def tdiff(D):
	file2 = sys.argv[3]
	tol2 = file2tokens(file2)
	file1 = sys.argv[2]
	tolk1 = file2tokens(file1)
	tolk2 = []
	tolk3 = []
	for newf in tolk1:
		if newf[0] == 'COMMENT' or newf[0] =='NL' or newf =='NEWLINE':
			continue
		else:
			tolk2.append(newf[0])
	
	for newf2 in tol2:
		if newf2[0] == 'COMMENT' or newf[0] =='NL' or newf =='NEWLINE':
			continue
		else:
			tolk3.append(newf2[0])
			
	p = similarity(tolk2,tolk3)
	if p >= 0.6:
		print(p, 'The files are the same')
	else:
		print(p, 'The files are not the same')


def adiff():
	file7 = sys.argv[3]
	tol6 = file2tokens(file2)
	file8 = sys.argv[2]
	tolk7 = file2tokens(file1)
	tolk4 = []
	tolk5 = []
	for newf in tolk1:
		if newf[0] == 'COMMENT' or newf[0] =='NL' or newf =='NEWLINE':
			continue
		else:
			tolk2.append(newf[0])
	
	for newf2 in tol2:
		if newf2[0] == 'COMMENT' or newf[0] =='NL' or newf =='NEWLINE':
			continue
		else:
			tolk3.append(newf2[0])
			
	p = similarity(tolk2,tolk3)
	if p >= 0.6:
		print(p,'=> The files are the same')
	else:
		print(p,'=> The files are not the same')

# Returns a float indicating how closely matched the two sequences
# passed in as arguments are.  A result >= 0.6 should be a close match.
# for tdiff and adiff

def similarity(L1, L2):
	matcher = difflib.SequenceMatcher(None, L1, L2)
	return matcher.ratio()	
	
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
	except IOError:
		return None
	return tokens


def main():
	V = []
	if len(sys.argv) < 3:
		print('Usage: python3 as3.py danger file.py, python3 as3.py tdiff file1.py file2.py, python3 as3.py imports file.py, python3 as3.py adiff file1.py file2.py')
		return
	
	
	elif sys.argv[1] == 'import':
		if len(sys.argv) != 3:
			print('Error: wrong number of filenames')
			return
		tol = file2tokens(sys.argv[2])
		imp(tol)
	
	elif sys.argv[1] == 'danger':
		if len(sys.argv) != 3:
			print('Error:wrong number of filenames')
			return
		tol1 = file2tokens(sys.argv[2])
		dager(tol1)

	for filename in sys.argv[2:]:
		V.append(file2tokens(filename))	
	if sys.argv[1] == 'tdiff':
		if len(sys.argv) != 4:
			print('Error:wrong number of filenames')
			return
		tdiff(V)
		
	else:
		print('input name not recognize')
		
	
main()
