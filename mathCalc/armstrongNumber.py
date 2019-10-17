#! python3
import sys
number = 0


# split number and append it into the list.	
def splitNumber(lst, num):	while(num > 0):
		remainder = num % 10
		num = num // 10
		lst.append(remainder)
	
def reverseList(lst):
	return lst.reverse()
	



def power(value, sign):
	return pow(value, sign)

def is_armstrong(lst, number):
	value = 1
	sum = 0
	isOk = False
	print("Number: ", number)
	while(sum < number):
		value += 1
		sum = 0
		for i in lst:
			sum += power(i, value)
			isOk = True
	if number == sum:
		print(number, " is an armstrong number.")
		for i in lst:
			print(i," ^ ", value, " = ",(pow(i, value)))
	else:
		print(number, " is not an armstrong number.")

def processOperation(number):
	num = number
	lst = []	
	splitNumber(lst, num)
	reverseList(lst)
	is_armstrong(lst, number)
	lst.clear()
	
try:
	number = sys.argv[1]
except:
	number = int(input("Enter number: "))
ch = "yes"

while ch.lower() == "yes" or ch.lower() == "y":
	processOperation(number)
	print("="*40)
	ch = str(input("Do you want more iteration? \nSuggestion: (if yes type 'yes' or 'y'):"))
	if ch.lower() == "yes" or ch.lower() == "y":
		number = int(input("Enter number: "))
	else:
		print("Bye bye!")
	
	