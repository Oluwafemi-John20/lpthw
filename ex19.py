# A function that takes two arguement which are cheese count and boxes of crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have %d cheeses!" % cheese_count)
	print("You have %d boxes of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get a blanket. \n")


# We are passing integers into the function.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#We are creating variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# We are passing the variables created into the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# We added expression into the function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# We are combine the variables and integers
print("And wecan combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)