################################
######### Excercise 13##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Running scripts using import statements in Python
'''

#This program will take the script, username and password as arguments to run in the python file
#If the username and password entered by the user in the arguments match with the programs username and password, then a correct message will display to the user!

from sys import argv

script_name, username, password = argv


if username == "schachte" and password == "zieser1l12":
    print 'Those credentials were correct for the program!'
else:
    print 'Sorry, that input was incorrect!'




#This allows you to add multiple arguments the run command when inputting the variables and script name in the console
#In console the run command would look like this:

#   python script_name.py var1 var2 var3

#You must fulfill the required arguments in the file for the file to run properly

'''
Study Drills
'''

#When inputting less arguments that the program specifies, the output is this error
'''
Traceback (most recent call last):
  File "Assignment13.py", line 13, in <module>
    script_name, first_var, second_var, third_var = argv
ValueError: need more than 2 values to unpack
'''

#Needing two more values to unpack means that the amount of variables in the argument didn't satisfy the full (3) requirements.
#Adding two more arguments into the run command would output a correct statement.

'''
Change your file to accept user input into the args and then output based on the user input into the arguments
'''
