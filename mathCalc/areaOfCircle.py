#! python3

import sys
import math

radius = 0
try:
	radius = sys.argv[1]
except:
	radius = float(input("Enter radius: "))
	
	
	area = math.pi * math.pow(radius, 2)print("The area of circle is ", area)