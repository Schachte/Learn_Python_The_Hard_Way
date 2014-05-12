################################
######### Excercise 35##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

from sys import exit
'''
Working with branches and functions in Python
'''


#Use functions to describe different rooms of a house.
#User can enter the rooms and examine different features using functions


def entry():
    welcome_message = '''

    Welcome to the entry way of the house!
    A) Enter the office
    B) Enter the kitchen
    C) Exit the house
                      '''


    print welcome_message

    option = raw_input(">>")

    if 'A' in option or 'a' in option or 'office' in option:
        office()
    elif 'B' in option or 'b' in option or 'kitchen' in option:
        kitchen()
    else:
        print 'Ok we will now exit the house!'
        exit()


def office():
    print 'You are now in the presence of the users office. Would you like to leave or look at the computer?'
    user_option = raw_input(">>")

    if 'leaves' in user_option or 'leave' in user_option or 'Leave' in user_option:
        print 'Ok, we will leave'
        entry()
    elif 'computer' in user_option or "look" in user_option:
        print 'This is a nice custom built computer in the users office!'
        print 'We will now exit the office!'
        entry()

def kitchen():
    print 'Hello! You are now in the users kitchen. Would you like to see the pantry?'
    user_option = raw_input(">>")

    if 'pantry' in user_option or 'yes' in user_option or 'Yes' in user_option:
        print 'You are now in the pantry! Yummy food!'
        print 'We will now exit the pantry and the kitchen!'
        entry()
    elif 'no' in user_option or 'No' in user_option or 'exit' in user_option or Exit in user_option:
        print 'We will now exit the area and return back to the main living area!'
        entry()

looping = True

while (looping):
    entry()
