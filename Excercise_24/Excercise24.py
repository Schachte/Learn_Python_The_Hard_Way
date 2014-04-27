################################
######### Excercise 24##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Combine all excercises into a functional application
'''

from sys import argv            #Allows user to specify all the initial arguments for the program to run properly
from os.path import exists      #Checks if a file exists when reading, writing, closing or opening a file

script, filename, copy_to_file = argv


def welcome():
    #Use of escape sequence to output string data to the console
    return 'Welcome to Ryan Schachte\'s Learn Python the Hard Way application!'

#Define a function to open a filename from the arguments
def open_file(filename):
    #If the file exists in the directory, then print "Exists"
    if exists(filename):
        print 'Ok, the file does exist, so I will try and open it!\n'
        #Open the users file and store into user_file var
        user_file = open(filename)
        #Success Message
        print '%s was opened successfully!\n' %(filename)
        #Return the opened file
        return user_file
    else: #If non-existent in the dir, then print error msg
        print 'File does not exist in the directory specified'

#Call the user function and store return val into read_contents variable
read_contents = open_file(filename)

#If the initial file does exist in the dir, then print out contents of file.
if exists(filename):
    print read_contents.read()

''''''''''''''''''''''''''''''

#Get random information from user
prompt = ">>>"
print 'What is your name?'
name = raw_input(prompt)

print 'Where do you live?'
location = raw_input(prompt)

print 'What is your major?'
major = raw_input(prompt)

#String format and concatenate user info into var
information = '''
Your name is %s.
You live in %s.
Your major is %s.
''' %(name, location, major)

#Display user info in nice fashion
print 'I am going to write the following information to the file:\n'
print information

#Open file in write mode
file_opener = open(filename, "w")

#Write the formatted statement into txt file
file_opener.write(information)
print 'Information written to file, would you like to view the file contents? Return to view: '
raw_input()

#Close previous file
file_opener.close()

#Open file in read mode
file_opener = open(filename, "r")

#Assign display var to read info
file_display = file_opener.read()

#Print the display var
print file_display

#Close file
file_opener.close()

#Copy data to another file
print 'Just to be on the safe side, we are going to copy the data to another file.'
print 'We are copying the data from %s to %s' %(filename, copy_to_file)

#Open file in read mode to get data from file
file_opener = open(filename, "r")
print 'The file "%s" is opened.' %(filename)

#Store file data
file_data = file_opener.read()

#Close file
file_opener.close()

#Open file in writeable mode
new_file_opener = open(copy_to_file, "w")

#Write the string data into the file and output success message
new_file_opener.write(file_data)
print 'Data written to "%s" successfully!' %(copy_to_file)



