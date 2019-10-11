#! python3
# Python nonlocal and global keyword
def counter():
	num = 0
	def incrementer():	# internal function
		nonlocal num # nonlocal keyword
		num += 1
		return num
	return incrementer
	
	
c = counter()
print(c()) 
print(c())
print(c())

# global function

x = 0

def Ex():	
	global x
	x = 10
	return x
	
print(Ex())
print(x)

# without global

def Ex1():
	x = 15
	return x
	
print("Non global ",Ex1())
print("Non global ", x)