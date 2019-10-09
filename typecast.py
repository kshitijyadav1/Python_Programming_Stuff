#! python3
name = str(input("Enter your name: "))
print("Your name is", name)
age = str(int(input("Enter your age: "))) # first int get the number and str convert it into string
# THE ABOVE LINE USING TYPECASTING
print("Your age is", age)
room_temperature = float(input("Enter envrironment temperature (in celsius): "))
print("Your body dealing with", room_temperature, "degree celsius environment temperature.")
length_of_name = len(name)
print("Your name length is", str(length_of_name))
print("The round of temperature value is", str(round(room_temperature)))
