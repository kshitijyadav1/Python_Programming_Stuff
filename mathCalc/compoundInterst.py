#! python3
# calculate compound interest = p(1 + R(100))^r
import sys


try:
	principal = float(sys.argv[1])
	rate = float(sys.argv[2])
	time = float(sys.argv[3])
except:
	principal = float(input("Enter principal: "))
	rate = float(input("Enter rate: "))
	time = float(input("Enter time: "))
	
	
print("Compound Interest : ", compoundInterest)
