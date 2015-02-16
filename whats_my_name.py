#input from text file
import fileinput
#declare multiple variables
first_name, last_name = fileinput.input()
first_name = first_name.strip()
last_name = last_name.strip()

#Solve and output
print("Hello %s %s! You just delved into python." % (first_name, last_name))
