import random
for i in range(1,1999):
	print("%4d"%random.randint(10000,99999),end=' ')
	if i % 10 == 0:
		print()