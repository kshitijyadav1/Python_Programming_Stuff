#! python3
# -v python 3.7
import sys
import math
import timenumberOfSide = 0
side = 0
INITtime = time.time() 
try: 
	numberOfSide = sys.argv[1]
	side = sys.argv[2]
except:
	numberOfSide = float(int(input("Enter the number of sides: ")))
	side = float(input("Enter the side: "))
	
	area = (numberOfSide * math.pow(side, 2)) / (4 * math.tan(math.pi / numberOfSide))
print("The area of the polygon is ", area)

TERMtime = time.time()
totalSecond = int(TERMtime - INITtime)
totalMS = (TERMtime - INITtime) - totalSecond
convert = str(totalMS).split('.')

print("Total estimated time: ", totalSecond, "seconds.",end='')
print("and", convert[1], " microseconds.")
