################################
######### Excercise 29##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################
#Implement a what if statement for python to execute certain code under certain condition


'''
Initial Assignments to children and adults
'''
adults = 30
children = 40

'''
Using basic if-else statements
'''
if adults > children:
    print 'Adults are greater!'
else:
    print 'Children are greater!'

adults += 10 #Increment the initial pre-defined value of the adults to change the program output

if adults > children:
    print 'Adults are greater!'
elif adults < children:
    print 'Children are greater!'
else:
    print 'Children and adults are equal in quantity'




