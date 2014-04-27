################################
######### Excercise 20##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

from sys import argv

'''
This is file reading using user-defined arguments from the argv module in the sys library and opening files using functions in python
'''

#Initial arguments to pass into the terminal
script, file_open = argv

#Function displaying available functions in the program
def menu():
    print '''
        A: Open File
        B: Close File
        C: Read File
        '''

    #Get the users choice
    choice = raw_input(">>>")
    choice = choice.lower()
    return choice

#Open the file in the args
def open_file(fileopen):
    openme = open(fileopen)
    return openme

#Close the file in the args
#This function is not fully implemented
def close_file(fileclose):
    print 'File is closed'
    return fileclose.close()

#Make program loop forever
loop = True
while (loop):

    #Display menu after each option is inputted
    choice = menu()

    #Run different functions based on the input of the user

    if (choice == "a"):
        open_file(file_open)
        print 'File is opened!'

    elif (choice == "b"):
        close_file(open_file(file_open))

    elif (choice == "c"):
        print 'Here are the contents of the opened file: '
        information = open_file(file_open).read()
        print information


