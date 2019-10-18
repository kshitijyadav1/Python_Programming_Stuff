#! python3
import sys
# check fibonacci number
number = 0
try:
	number = sys.argv[1]
except:
	number = int(input("Enter number to check whether it is fibonacci or not (exception > 10000): "))

def checkFib(num):
	first = 0
	second = 1
	total = 1
	if num == 0:
		return True
	elif num == 1:
		return True
	else:
		for i in range(2, 10000):
			total = first + second
			first = second
			second = total
			if second == num:
				return True
		else:
			return False
if checkFib(number):
	print("Yes, ", number," is a fibonacci number.")
else:
	print("No, ", number," is not a fibonacci number.")
	