################################
######### Excercise 05##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#This is more advanced string concatenation

my_name = "Ryan Schachte"
my_age = 19
number_of_computers = 3
cat_name = "Ben"
dog_name = "Joey"

#%d is used for using integer and float substitution in concatenation
#%s is used for string replaced in concatenation

print "My name is %s and my cats name is %s and my dogs name is %s" % (my_name, cat_name, dog_name)
print "I have %d computers and I am %d years old" %(number_of_computers, my_age)
print "%d + %d" % (number_of_computers, my_age), " = ", number_of_computers + my_age

#Use parethesis when concatenating multiple sets of data/strings/etc
#Add a % moodulis when denoting data concatenation