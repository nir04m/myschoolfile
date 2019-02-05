bm = [
    [ 1, 0, 0, 0, 1 ],
    [ 1, 1, 0, 0, 1 ],
    [ 1, 0, 1, 0, 1 ],
    [ 1, 0, 0, 1, 1 ],
    [ 1, 0, 0, 0, 1 ]

]

for lst in bm:
	row=" "
	for digit in lst:
		if digit == 1:
			row = row + "x"
		else:
			row = row + " "
	print(row)

print()

#mirror image,no mod
for lst in bm:
	row=" "
	for digit in lst:
		if digit == 1:
			row = "x" + row
		else:
			row = " " + row
	print(row)


for i in range(len(bm)):
	temp =[]
	for j  in range(len(bm[i])):
		temp.append(bm[i].pop())
	bm[i]= temp