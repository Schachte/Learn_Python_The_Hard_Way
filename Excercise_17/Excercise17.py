################################
######### Excercise 17##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#Allows arguments in terminal to be pre-specified
from sys import argv

#Allows you to check if file currently exists on the drive
from os.path import exists

#Specifying arguments for running file (script name, file to copy from and file to copyto)
script, file, copytofile = argv

#Opens the initial file containing the data
open_initial = open(file)

#Stores contents of file into variable
file_data = open_initial.read()

#Stores length of the file
file_length = len(file_data)

#Prints file size data
print 'The file is %d bytes' %file_length

#Tells user if file exists or not
if exists(copytofile):
    print 'The copy_to file does exist!'
else:
    print 'Sorry, the copy_to file does NOT exist! However, it will be created'

raw_input('Would you like to continue? Enter to cont:')

#Opens the file to copy data into and makes it a writable file type
open_copy = open(copytofile, "w")

#Write the stored string data from initial file
open_copy.write(file_data)

#Print success write message
print 'Data written from %s into %s successfully!' %(file, copytofile)

#Close each file to ensure data writes appropriately
open_initial.close()
open_copy.close()

