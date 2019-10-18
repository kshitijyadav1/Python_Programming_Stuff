#! python3
import sys
# fibonacci number
number = 0try:
	number = sys.argv[1]
except:
	number = int(input("Enter number: "))
	
	def fiboNumber(val):
	total = 0
	first = 0
	second = 1
	if val == 0:
		return val
	elif val == 1:
		return val
	else:
		for i in range(2, val):
			total = first + second
			first = second
			second = total
		return second
	
print(fiboNumber(number))
			