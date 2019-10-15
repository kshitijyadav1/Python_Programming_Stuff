#! python3
import sys
# Simple interest  = (Principal * rate * time) / 100
principal, rate, time = 0, 0, 0
try:
	principal = float(sys.argv[1])
	rate = float(sys.argv[2])
	time = float(sys.argv[3])
except:
	principal = float(input("Enter principal: "))
	rate = float(input("Enter rate of interest: "))
	time = float(int(input("Enter time: ")))
	
simpleInterest = (principal * rate * time) / 100.0

print("Principal amount: ", principal)
print("Rate of interest: ", rate)
print("Time period: ", time)
print("Total simple interest is ", simpleInterest)
 	