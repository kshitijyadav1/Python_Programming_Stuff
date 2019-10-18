#! python3import sys
from_ = 1
to_ = 10
try:
	from_ = sys.argv[1]
	to_ = sys.argv[2]
except:
	from_ = int(input("Enter prime number from: "))
	to_ = int(input("Enter prime number to: "))

def findPrimeNumber(init, end):
	for val in range(init, end + 1):
		if val > 1:
			for n in range(2, end):
				if val % 2 == 0:
					break
			else:
				print(val)
					
					
					findPrimeNumber(from_, to_)