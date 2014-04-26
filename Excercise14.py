################################
######### Excercise 14##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################


'''
Make a program that takes arguments in the terminal from the user and then print questions (while passing arguments into the raw_input statement)
'''

from sys import argv

script_name, full_name = argv

prompt_initial = '>>>'

full_name = full_name.title() #Converts each word in full name to capitalize

print ''
print 'Hello %s, you are currently running the script %s!' %(full_name, script_name)
print 'Because this is the %s script, I am going to be asking you a few questions..' %(script_name)
print 'Question 1: Do you like me, %s?' %(full_name)


like_me = raw_input(prompt_initial)

like_me = like_me.lower() #lowers the answer, regardless of input since it's not a proper noun and outputs in middle of sentence

print 'Question 2: Where do you live, %s' %(full_name)

location = raw_input(prompt_initial)

location = location.title() #Capitalizes the location you live

print 'Question 3: What kind of computer do you have, %s' %(full_name)

computer_type = raw_input(prompt_initial)

computer_type = computer_type.title() #Capitalizes brand of computer you own

output = '''
Ok, so after running the %s script, I can see your full name is %s and you live in %s.
I can see that your status on liking me is %s and that the kind of computer you have is a %s. Nice.
''' %(script_name, full_name, location, like_me, computer_type)

print "%s" %output #prints output using string formatting technique... not totally necessary in this case since I could have just printed the variable
