################################
######### Excercise 11##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Build a raw input based user input program
'''

'''List of Errors Made'''
#String formatted incorrectly
#Didn't convert integer input to string and or integer from input

'''Potential Question'''
#Can you use string formatting operators in raw_input for string replacement/substitution?
#Link To Question : http://stackoverflow.com/questions/23199580/string-replacement-using-modulo-in-python-for-raw-input

name = raw_input("Hello, what is your name?")
age  = raw_input("Ok, " + name + " what is your age?")
residence = raw_input("Ok, so your name is " + name + " and you are " + age + " years old. Where do you live?")

user_data = """
\tYour name is: %s\n
\tYour age is: %d years old\n
\tYou reside in: %s""" % (str(name), float(age), str(residence))

print user_data