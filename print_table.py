# This program is used to print table
initPoint = int(input("Enter the table initializing number: "))
termPoint = int(input("Enter the table terminating number: "))
table = int(input("Enter the table number, to be print on screen: "))
for i in range(initPoint, (termPoint + 1)):
	print(table, "x", i, "=", (i*table))
	
