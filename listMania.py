#! python3
# list method
lst = []
def insert(key, data):
	lst.insert(key, data)

def remove(data):
	if data in lst:
		lst.remove(data)
	else:
		print("Invalid key")
		
def append(data):
	lst.append(data)
	
def show(key):
	return lst[key]
	
def showAll():
	return lst
	
def index(data):
	return lst.index(data)
	
def length():
	return len(lst)

def count(data):
	if data in lst:
		return lst.count(data)
	else:
		print("Insufficient match")
	
def reverse():
	return lst.reverse()
	
def pop():
	if len(lst) > -1:
		lastItem = lst[len(lst) - 1]
		lst.pop()
	else:
		print("List empty.")
		
def title():
	print(" "*10, "Welcome to the list mania")
	
def body():
	print("0 => quit")
	print("1 => Insert item.")
	print("2 => Remove item.")
	print("3 => append item.")
	print("4 => show item at the specified index.")
	print("5 => show All item.")
	print("6 => Get index of item.")
	print("7 => get length of list.")
	print("8 => count the same number of data.")
	print("9 => reverse the list")
	print("10 => Remove at the last(pop)")
	
title()
body()
opt = int(input("Enter option: "))
while opt != 0:
	if opt == 1:
		key = int(input("Enter key: "))
		print("", key, " = ",show(key), " The key value change with below entered value.")
		data = input("Enter data: ")
		insert(key, data)
	elif opt == 2:
		data = input("Enter data:")
		remove(data)
	elif opt == 3:
		data = input("Enter data: ")
		append(data)
	elif opt == 4:
		index = int(input("Enter key(index): "))
		print(show(index))
	elif opt == 5:
		print(showAll())
	elif opt == 6:
		key = input("Enter key(index): ")
		print(index(key))
	elif opt == 7:
		print("The length of the list is", length())
	elif opt == 8:
		data = input("Enter data: ")
		print(count(data))
	elif opt == 9:
		print(reverse())
	elif opt == 10:
		pop()
	body()
	opt = int(input("Enter option: "))
	




	