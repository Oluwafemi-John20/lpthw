def print_while_loop(iterations = 6, increments = 1):
	i = 0
	numbers = []

	while i < iterations:
		print("At the top i is %d" % i)
		numbers.append(i)
	
		i = i + increments
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % i)
	print("The numbers:")

	for  num in numbers:
		print(num)