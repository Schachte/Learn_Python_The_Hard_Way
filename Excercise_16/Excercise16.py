################################
######### Excercise 15##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Basic file writing
Program will do the following:
    User types in script name, filename and user name
'''

from sys import argv

script_name, filename, student_name = argv

#opened file and "w" allows it to be open and writable
#opened file with "r+" allows you to read AND write to it without closing and reopening
target = open(filename, "r+")
print '%s is now opened in the program!' %(filename)

print 'Hello %s, we are going to organize your life a bit!' %student_name

class_name = raw_input("Enter Class Name >>>")
homework_name = raw_input("Enter Homework Name >>>")
due_date = raw_input("Enter Due Date >>>")

file_output = '''
Alright %s, here is the calendar information.\n
\tClass Name: %s
\tHomework: %s
\tDue Date: %s
''' %(student_name, class_name, homework_name, due_date)

#Write string data to file
target.write(file_output)
#Close the file
target.close()

#Open file for reading
target = open(filename, "r")
#Prting contents of the file
print target.read()






