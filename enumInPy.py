from enum import Enum
class Color(Enum):
	"""
	Enums have been backported from python 3.4. You can get this the enum34 backport from PyPI.
	pip install enum34
	 
	"""
	red = 1
	green = 2
	blue = 3
		print(Color.red)
print(Color(1))
print(Color(2))
print(Color['blue'])