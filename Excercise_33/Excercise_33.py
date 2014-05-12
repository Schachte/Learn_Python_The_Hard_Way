################################
######### Excercise 33##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#Gain exit conditional input from the user

print 'Loop Count?' #Count number of times user would like to loop through string format
exit_conditional = raw_input('>>')
exit_conditional = float(exit_conditional) #Convert exit_conditional string into a float

count = 1

while (count <= exit_conditional):
    print 'Current count is at: %d' %(count) #Display the data
    count = count + 1 #Count increments to make sure the loop stops at the appropriate position
