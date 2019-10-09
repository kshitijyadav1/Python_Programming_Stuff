#! python3
# Stack overview program. with built-in method
import sys

lst = []

def push(number):
	if len(lst) <= 10:
		lst.append(number)
	else:	
		print("Stack overload")
		

def pops():
	remove_element = 0
	if len(lst) > 0:
		remove_element = lst[len(lst) - 1]
		lst.pop()
		print("The list element value is ", remove_element, " has been removed.")
	else:
		print("The list is empty.")
	
def is_empty():
	if len(lst) == 0:
		return True
	else:
		return False

def length():
	return len(lst)

def top():
	return lst[0]

def show():
	print(lst)

def title():
	print("Stack operation")

def body():
	print("0 => quit")
	print("1 => push")
	print("2 => pop")
	print("3 => len")
	print("4 => is_empty")
	print("5 => top")
	print("6 => show")

if __name__ == '__main__':
	opt = 6
	title()
	while opt != 0:
		try:
			body()
			opt = int(input("Enter option: "))
			print("Ok, your request is processing.")
			if opt == 0:
				print("Bye bye, thanks for trying.")
				sys.exit()
			elif opt == 1:
				print("Push value in stack")
				try:
					value = int(input("Enter value in stack "))
					push(value)
				except:
					print("There was just an issue, when push value in stack.")
			elif opt == 2:
				print("Pop value in stack")
				pops()
			elif opt == 3:
				print("The length of stack is ", length())
			elif opt == 4:
				if is_empty():
					print("Yes, the stack is emtpy.")
				else:
					print("No, the stack is not empty.")
			elif opt == 5:
				print("The top stack reference is", top())
			elif opt == 6:
				show()
			else:
				print("Incorrect input.")
		except:
			pass

	