# This program says Hello and asks for my name.

print('Hello World!')
print('What is your name?') # ask for name
myName = input()
print('it is good to meet you, ' + myName)
# I want to add a function here that formats the String myName to have a Capitol letter first.
print(myName + ' what is your age?') # ask for age
myAge = input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')
