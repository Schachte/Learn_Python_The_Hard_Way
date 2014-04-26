################################
######### Excercise 19##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
PIZZA EAT
File takes in slices of pizza into initial command-line args.
User specifies the number of slices to begin with.
The user can eat the pizza
'''

#Import ability to define initial terminal arguments entered by the user
from sys import argv

#Defining initial terminal args
script_name, pizza_count = argv

#Converting count string to an integer
pizza_count = int(pizza_count)

'''
These are all the function declarations that control the flow of the program
'''

#Initial declaration to say hello to the user
def initial(slices):
    print 'Ok, you are beginning with %d slices of pizza!' %slices
    print 'Lets begin eating!\n'

#The eat function will decrement the slice count by 1
def eat(slices):
    print 'You eat a slice of pizza\n'
    slices = slices - 1
    return slices

#This will print the number of slices left for the user to eat
def print_count(slices):
    print 'The number of slices remaining is: %d slices\n' %slices

#Allows the main loop to operate based on boolean values
def eat_more_pizza():
    eat_more = raw_input("Eat pizza?")
    eat_more.lower()

    if (eat_more == "yes" or eat_more == "y"):
        eat_more = True
        return eat_more

    elif (eat_more == "no" or eat_more == "n"):
        eat_more = False
        print 'You are now done eating pizza!'
        return eat_more

    else:
        print 'Invalid input!'

#Welcome the user
initial(pizza_count)

#Initial start to boolean loop
eat_more = eat_more_pizza()

while (eat_more == True):

#If the user wants to eat more and there are still slices left in the box, then have the user eat the pizza
    if (eat_more == True and pizza_count > 0):
        pizza_count = eat(pizza_count)
        print_count(pizza_count)
        eat_more = eat_more_pizza()

#Exit if the box is empty
    else:
        print 'There is no more pizza left!'
        break










