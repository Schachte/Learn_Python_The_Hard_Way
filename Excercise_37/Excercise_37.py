################################
######### Excercise 37##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#Description:
#Using and understanding unknown symbols, logic statements and escape sequences in Python

#**********************
#*****del kwrd*********
#**********************

'''
Del is used to recrusively delete information from left to right.
This is used to remove specified elements from a list in Python
'''

#**********************
#*****del example******
#**********************

user_data = ['Index 0', 'Index 1', 'Index 2', 'Index 3']
print user_data
del user_data[0]
print user_data

#Console output
'''
['Index 0', 'Index 1', 'Index 2', 'Index 3']
['Index 1', 'Index 2', 'Index 3']
'''

#**********************
#*****global keywrd****
#**********************

'''
global vars are seldom required unless explicity required by the function.
Global variables aren't preferred because it can ruin the general understanding of a basic program structure
'''

#Global kwrd example:

'''

def random_function():
    global var_name
    var_name = 'This is a global variable that can be accessed by the entire program (Even out of the function)

print var_name
'''

#Because you are designating specific variables to be global, they can be printed and accessed outside or inside a function
#The expected output for the following (above) code would print out the var_name.
#This is simply because the var_name is global. If the var name wasn't declared as global in the function, then
#program console would output an error


#**********************
#*****with keywrd*****
#**********************

'''
With keyword is often in file streams. Minimizes the amount of code needed to write when opening and closing file streams in python
'''

#**********************
#*****with example*****
#**********************
'''
 with open('output.txt', 'w') as f:
     f.write('Hi there!')
'''

#The following code would opena writeable version of the output text file.
#Once the specified data has been written to the file, the file will automatically close itself because it was
#opened using the with keyword.

#**********************
#*****assert keywrd****
#**********************

'''
Assert is often used to test conditionals that should NEVER happen
'''


#**********************
#*****assert example***
#**********************

current = 'Test'
assert current == 'True', 'error!'

'''
Assert statements are structured in the following form: <assert (condition), (AssertionError)>
'''

#If the condition based off the assertion statement is false, then the assertion error will be rasied



