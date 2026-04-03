# This inserts the string 10 into the placeholder character %d
x = "There are %d types of people." % 10

# Created a variable binary
binary = "binary"

# Created a variable do_not for "don't"
do_not = "don't"

# Created a variable y, which two strings were inserted binary and do_not.
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints x
print x
# Prints y
print y

# Prints the the string and replaces the placeholder %r with variable x
print "I said: %r." % x
# Prints the string and replaced the placeholder %s with y.
print "I also said: '%s'." % y

#Created a variable hilarious
hilarious = False
# Created a variable using the string formating %r.
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints the joke_evaluation variable and replaces the %r with the variable stored in hilarious.
print joke_evaluation % hilarious

# Created a variable w
w = "This is the left side of..."
# Created a variable e
e = "a string with a right side."

# Prints the addition of strings in variable w and e.
print w + e

# The addition of two strings w and e makes a longer string because strings are concatenated upon addition in python.
#%r is used in debugging because it displays the raw data wile %s and displays to users.