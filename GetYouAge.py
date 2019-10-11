#! python3
from datetime import datetime, timedelta
def getDate():
	""" This method is used to set date,
	Year, Month, Day	"""
	print("Enter you date of birth and time.")
	year = int(input("Enter year(e.g. 1997): "))
	month = int(input("Enter month(e.g. 1-12): "))
	day = int(input("Enter day(e.g. 1-31): "))
	hour = int(input("Enter hour(e.g. 0-23): "))
	minute = int(input("Enter minute(e.g. 0-59): "))
	second = int(input("Enter second(e.g. 0-59): "))
	return year, month, day, hour, minute, second
	
	
YEAR, MONTH, DAY, HOUR, MINUTE, SECOND = getDate()
now = datetime.now()
then = datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND)
delta = now - then
print("You are ", delta, " old")
print(delta.days)
elapsedDays = delta.days
elapsedSeconds = delta.seconds
elapsedMS = delta.microseconds

currentYear = int(datetime.now().year)totalYear = currentYear - YEAR
currentMonth = int(datetime.now().month)
currentDay = int(datetime.now().day)
totalMonth = currentMonth - MONTH
totalDay = currentDay - DAY

print("Now, you are ",end=' ')
print("Total Year: ", totalYear,end=' ')
print("Total Month: ", totalMonth,end=' ')print("Total Day: ", totalDay,end=' ')
print("Total hour: ", delta.seconds,end=' ')
print("Total microseconds: ", delta.microseconds, end=' ')
print("old.")