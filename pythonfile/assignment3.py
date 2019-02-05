import sys
D ={}
#function of import 
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

# function of danger
def danger(l3):
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

#function of tdiff
def tdiff(D):
	#putting the files in a list
	P = sys.argv[2]
	l1 = file2tokens(P)
	H = sys.argv[3]
	l2 = file2tokens(H)
	tolk2 = []
	tolk3 = []
	
	for f in l1:
		if f[0] == 'COMMENT':
			continue
		if f[0] == 'NL':
			continue
		if f[0] == 'NEWLINE':
			continue
		else:
			tolk2.append(f[0])
	
	for f2 in l2:
		if f2[0] == 'COMMENT':
			continue
		if f2[0] == 'NL':
			continue
		if f2[0] == 'NEWLINE':
			continue
		else:
			tolk3.append(f2[0])
	#checking the similarity of the two list		
	score = similarity(tolk2,tolk3)
	if score >= 0.6:
		print(score, '=> The files are the same')
	else:
		print(score, '=> The files are not the same')

def adiff(S):
	W = sys.argv[2]
	f3 = file2tokens(W)
	D = sys.argv[3]
	f4 = file2tokens(D)
	tol4 = []
	tol5 = []
	for A1 in f3:
		if A1[1] not in ['COMMENT' , 'NL' ,'NEWLINE']:
			tol4.append(A1[1])
	
	for A2 in f4:
		if A2[1] not in ['COMMENT' , 'NL' , 'NEWLINE']:
			tol5.append(A2[1])
	
	score1 = similarity(tol4,tol5)
	if score1 >= 0.6:
		print(score1, '=> The files are the same')
	else:
		print(score1, '=> The files are not the same')
	
import token
import tokenize

# Returns a list of (token, attribute) tuples corresponding to the
# tokens in the input Python 3 filename passed as a parameter.  Assumes
# that the file actually does contain valid Python code.  Returns None
# in the event of any error.
# tokens file
def file2tokens(filename):
	try:
		f = open(filename, 'rb')
		tokens = []
		for t in tokenize.tokenize(f.readline):
			tokens.append( (token.tok_name[t.type], t.string) )
	except IOError:
		return None
	return tokens


import difflib

# Returns a float indicating how closely matched the two sequences
# passed in as arguments are.  A result >= 0.6 should be a close match.
# for tdiff and adiff
def similarity(L1, L2):
	matcher = difflib.SequenceMatcher(None, L1, L2)
	return matcher.ratio()

#running the code
def main():
	V = []
	if len(sys.argv) < 3:
		print('Usage: python3 as3.py danger file.py')
		print('Usage: python3 as3.py tdiff file1.py file2.py')
		print('Usage: python3 as3.py imports file.py')
		print('python3 as3.py adiff file1.py file2.py')
		return
	
	
	if sys.argv[1] == 'import':
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
		danger(tol1)
	elif  sys.argv[1] == 'tdiff' or sys.argv[1] == 'adiff':
		if len(sys.argv) != 4:
			print('Error wrong number of flenames')
			return

	for filename in sys.argv[2:]:
		V.append(file2tokens(filename))	
	if sys.argv[1] == 'tdiff':
		tdiff(V)
		return
	elif sys.argv[1] == 'adiff':
		adiff(V)
		return
		
	
	else:
		print('input name not recognize')
		
	
main()
