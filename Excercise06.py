################################
######### Excercise 06##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#initial variable assigned to a string of text. The % substitutes %d with a string. %d is a decimal and used for integers
x = "There are %d types of people." % 10

#The next two variables are string assignments specified by the programmer to their values, wrapped in quotes to designate them as strings
binary = "binary"
do_not = "don't"

#y is assigned to a string which contains a string format designated by modulo
y = "Those who know %s and those who %s." % (binary, do_not)

#We now send the data to the console with the print statement
print x
print y

#Printing formmated string with modulo replacements
print "I said: %r." % x
print "I also said: '%s'." % y

#hilarious is a boolean assigned to false
hilarious = False

#joke is assigned to a string. The %r modulo means escape characters are ignored.
joke_evaluation = "Isn't that joke so funny?! %r"

#print the previous string
print joke_evaluation % hilarious


w = "This is the left side of..."
e = "a string with a right side."

#this is an example of string concatenation in python.
#This is why the string is longer because you are concatenating two different strings into a single string
print w + e



