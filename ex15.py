# Import the argv library
from sys import argv

# Takes the arguements into variables
script, filename = argv

# Open the and save the content in txt
txt = open(filename)

# Prints the name of the file passed
print("Here's your file %r:"  %filename)
# Prints the content in txt
print(txt.read())

print("Tyoe the filename again:")
# Takes an input for the file
file_again = input("> ")

# Open the txt document again
txt_again = open(file_again)
# Prints the contents again
print(txt_again.read())