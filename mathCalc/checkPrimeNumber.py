#! python3
import sys
val = 1
try:
	val = sys.argv[1]
except:
	val = int(input("Enter number: "))
	
	
	if value > 1:
		for n in range(2, value):
			if value % 2 == 0:
				print("No,", value, " is not a prime number.")
				break
		else:
			print("Yes,", value, " is a prime number.")
			
			