#! python3
# find fibanocci number from the series init and to where the series end.
import sysfrom_ = 0
to_ = 0
try:
	to_ = sys.argv[2]
except:
	to_ = int(input("Enter the fibanocci series range: "))
	
	def n_Fibanocci_series(end):
	numberA = 0
	numberB = 1
	fib = 0
	for val in range(end):
		if val == 0:
			fib = numberA
			print((val + 1), " fibonacci number ",fib)
		elif val == 1:
			fib = numberB
			print((val + 1), " fibonacci number ",fib)

		elif val > 1:
			fib = numberA + numberB
			numberA = numberB
			numberB = fib
			print((val + 1), " fibonacci number ",fib)

		
print("="*31)		n_Fibanocci_series(to_)
		
		