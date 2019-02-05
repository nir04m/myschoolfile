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
	# No arguments given
	if len(sys.argv) == 1:
		# Print usage message and exit
		print("This program calculates the geometric mean or median of the data provided.")
		print("One argument ('mean', 'median', 'average', 'sum', or 'sort') is expected")
		print("Usage: geometric_mod.py mean < data or geometric_mod.py median < data")
		return
		
	# Wrong number of arguments	
	elif len(sys.argv) != 2:
		# Print error message and exit
		print("Error, incorrect number of arguments (1 expected)")
		return
		
	# Calculate and print geometric mean	
	if sys.argv[1] == "mean":
		print("Geometric mean: ", geoMean(readData()))
		
	# Calculate and print median	
	elif sys.argv[1] == "median":
		print("Median: ", median(readData()))
	
	# Calculate and print the sum	
	elif sys.argv[1] == "sum":
		print("Sum: ", sum(readData()))
		
	# Calculate and print average	
	elif sys.argv[1] == "average":
		print("Average: ", average(readData()))
		
	# Calculate and print sorted list	
	elif sys.argv[1] == "sort":
		print("Sorted: ", sort(readData()))
		
	# Function name not recognized	
	else:
		print("Error, argument must be 'mean', 'median', 'average', 'sum', or 'sort'")
	
main()
	

