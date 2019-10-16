#! python3
# calculate compound interest = p(1 + R(100))^r
import sys

principal, rate, time = 0,0,0
try:
	principal = float(sys.argv[1])
	rate = float(sys.argv[2])
	time = float(sys.argv[3])
except:
	principal = float(input("Enter principal: "))
	rate = float(input("Enter rate: "))
	time = float(input("Enter time: "))
	
	compoundInterest = principal * (pow((1 + rate / 100), time))
print("Compound Interest : ", compoundInterest)
