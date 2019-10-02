import sys
x = 0
y = 0
sign = 'n'
try:
	x = int(sys.argv[1])
	sign = str(sys.argv[2])
	y = int(sys.argv[3])
	
except:
	pass
if sign == 'n':	
		x = int(input("Enter the first number: "))
		y = int(input("Enter the second number: "))
		sign = str(input("Enter operator: "))
answer = 0
if sign == '+':
	answer = x + y
elif sign == '-':
	answer = x - y
elif sign == '*':
	answer = x * y
elif sign == '/':
	answer = x / y
elif sign == '//':
	answer = x // y
elif sign == '**':
	answer = x ** y

print(x, sign, y," = ", answer)
sys.exit()