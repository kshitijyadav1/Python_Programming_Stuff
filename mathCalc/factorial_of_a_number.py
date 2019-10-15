#! python3
import sys
number = 0
try:
	number = int(sys.argv[1])
except:
	number = int(input("Enter number: "))
print("File name: ", sys.argv[0])

# recursion function
def factorial(num):
	if (num == 1 or num == 0): # base condition
		return 1
	else:
		return num * factorial(num - 1)
	
print("Number: ", number)
print("Factorial: ", factorial(number))
	