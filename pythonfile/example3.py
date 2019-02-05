import sys


def readData():
	
	values = []
	val = input()
	while val != "end":
		values.append(int(val))
		val = input()
		
	return values
	
def geoMean(values):
	
	product = 1
	for val in values:
		product = product * val
		
	geomean = product ** (1/len(values))
	return geomean
	
def median(values):
	
	sortedList = sorted(values)
	med = 0
	if len(sortedList) % 2 == 0:
		val1 = sortedList[len(sortedList)//2]
		val2 = sortedList[len(sortedList)//2 - 1]
		med = (val1+val2)/2
	else:
		med = sortedList[len(sortedList)//2]
		
	return med

# Takes a list and returns that list sorted
def sort(values):
	return sorted(values)
	
# Takes a list and returns the sum of that list	
def sum(values):	
	total = 0
	for val in values:
		total = total + val
		
	return total
		
# Takes a list and returns the average of that list
def average(values):
	total = sum(values)
	avg = total / len(values)
	return avg	

def main():
	if len(sys.argv) == 1:
		print('Error: the program needs one argument either mean or median')
		print("One argument ('mean', 'median', 'average', 'sum', or 'sort') is expected")
		print('Usage: geometric_mod.py mean < data or geometric_mod.py median < data')
		return
	
	elif len(sys.argv) != 2:
		print('Error: the program needs only one argument  ')
		return
		
	if sys.argv[1] == 'mean':
		print("Geometric mean:",geoMean(readData()))
		
	elif sys.argv[1] == 'median':
		print("Geometric median:",median(readData()))
	
	# Calculate and print the sum	
	elif sys.argv[1] == "sum":
		print("Sum: ", sum(readData()))
		
	# Calculate and print average	
	elif sys.argv[1] == "average":
		print("Average: ", average(readData()))
		
	# Calculate and print sorted list	
	elif sys.argv[1] == "sort":
		print("Sorted: ", sort(readData()))
		
	else:
		print('input name not recognize')
	

main()
