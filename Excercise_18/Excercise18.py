################################
######### Excercise 18##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Make a program to ouput arguments in Python using function calls
'''

from sys import argv

script_name, arg1, arg2, arg3 = argv

def print_first(firstarg):
    print 'First Arg: %s' %(firstarg)

def print_first2(firstarg, secondarg):
    print 'First Arg: %s\nSecond Arg: %s' %(firstarg, secondarg)

def print_all(f,s,t):
    print 'First: %s\nSecond: %s\nThird: %s' %(f,s,t)

#Call each function in order
print 'Printing the first function:'
print_first(arg1)

print 'Printing the second function:'
print_first2(arg1, arg2)

print 'Printing the third function'
print_all(arg1, arg2, arg3)

