################################
######### Excercise 42##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

import urllib2

'''
Python script to cancel out swears and replace all letters with asterisks
Read the data and compare each word to the text file counter-part
'''

swear_list = [] #Store the list of words in this Python list here

data_website = 'file:///Users/rschacht/Documents/Programming/Learn_Python_The_Hard_Way_Excercises/Excercise_42/text_file.txt'

word_data = urllib2.urlopen(data_website)

print 'Please enter your sentence to test swearing validity:'

swear = raw_input('>>')

for each_item in word_data:
    if each_item in swear:
        print 'There is a swear word in this sentence!'


