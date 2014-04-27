################################
######### Excercise 21##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#Allows coder to specify initial args
from sys import argv

#Assining initial args
script_name, username = argv

#Get name from user
def name(username):
    your_name = 'Your full name is: %s' %username
    return your_name

#Get users age
def user_age():
    print 'Enter your age'
    age = raw_input(">>")
    return age

#Get location of the user
def user_location():
    print 'Enter your location'
    location = raw_input(">>")
    return location

#Concantetate all the information into a single string for the user to view the information nicely.
def information_concatenation(name, age, location):
    info = '''
        %s
        You are currently %s years old.
        You are located in %s
        ''' %(name, age, location)
    return info

#Assign the function output to variables so the information can be concatenated properly
full_name = name(username)
age = user_age()
location = user_location()

#Print the information of the user
print information_concatenation(full_name, age, location)