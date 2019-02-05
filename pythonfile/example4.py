import sys

print(sys.argv)
print(sys.argv[1])
if len(sys.argv) == 1:
	print("this program prints the arguments provided on the command line,")
	print()
if len(sys.argv) != 3:
    print("Error, 2 arguments expected. ")
