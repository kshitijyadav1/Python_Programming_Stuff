#! python3
#! -v python 3.7
import sys
import math
radius = 0
vertex = 5
try:
	radius = sys.argv[1]
	vertex = sys.argv[2]
except:
	radius = float(input("Enter the length from the center to the vertex: "))
	vertex = int(input("Enter the number of vertices: "))
	
if vertex <= 0: 
	vertex = 5
	print("Pentagon have 5 vertices.")
	
side = 2 * radius * math.sin(math.pi / vertex)
side = math.pow(side, 2)
area = (3 * math.sqrt(3) * side) / 2.0
print("The area of pentagon is,", area)