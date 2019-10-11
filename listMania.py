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
	
def reverse(nlst):
	nlst = lst.reverse()
	
def pop():
	if len(lst) > -1:
		lastItem = lst[len(lst) - 1]
		lst.pop()
	else:
		print("List empty.")
		
