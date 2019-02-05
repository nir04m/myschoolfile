import random

SENTINEL = 'THE\tEND'

L1 = []
L2 = []

while True:
	line = input()
	if line == SENTINEL:
		break

	words = line.split('\t')
	L1.append(words[0])
	L2.append(words[1])

random.shuffle(L1)
random.shuffle(L2)

for i in range(len(L1)):
	print(L1[i], 'and', L2[i])

