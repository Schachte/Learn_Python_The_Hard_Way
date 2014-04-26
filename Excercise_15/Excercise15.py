################################
######### Excercise 15##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Program that will read file input from string args define by the user in terminal
'''

#imports argv, which allows you to specify more than the default script run command
from sys import argv

#Chronologically assigning the arguments to the initial terminal run
script_name, file_name = argv #Arguments are pre-defined to take in script name and then the file user wants to open

#Printing basic string formatting off argv defined by the user
print 'The script %s will attempt to open and read the file %s' %(script_name, file_name)

#Opens file within the program
file_open = open(file_name)

#Success message -- Not very good, because it won't catch errors
print 'The file was successfully opened! Would you like to open the file, y/n?'

#Prompts user to open the file while also passing strings in the parameters of the raw_input
openfile = raw_input(">>>") #String boolean to determine if the file should be read


#Simple conditionals that will or will not read contents of the file
if (openfile == "y"):
    output = file_open.read()
    print output
elif (openfile == "n"):
    print 'Ok, the file will not be read'
else:
    print 'That input was invalid'

#Allowing more options to open, close or read files
print 'Ok, we can open, close or read another file as well, which would you like to do?'
print 'A: Close File\nB: Open Another File\nC: Read File'
option = raw_input(">>>")

#Converting option to lower case for easier conditonal assignments
option = option.lower()

#4 part conditional with reading and closing file functions
if option == "a":
    file_open.close()
    print 'Ok, the file was closed!'

elif option == "b":
    file_name.close()
    new_file = raw_input("What is name of the new file?")
    open(new_file)
    print new_file.read()

elif option == "c":
    print file_open.read()

else:
    print 'Invalid option'
