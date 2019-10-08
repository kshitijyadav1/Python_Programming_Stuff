#! python3
print("*"*10, "Age condition", "*"*10)
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
def age_classification(age):
	if age >= 0 and age <= 12:
		return "Child"
	elif age >= 13 and age <= 18:
		return "Adolescence"
	elif age >= 19  and age <= 59:
		return "Adult"
	elif age >= 60: 
		return "Senior Adult"
	else:
		return "Not Defined."
print("Your name is", name)
print("You are", age, " years old and you are", end='')
str = str(age_classification(age))
vowel = ['a','e','i','o','u']
if str[0].lower() in vowel:
	print(" an ", str, ".", sep='')
else:
	print(" a ",str, ".", sep='')