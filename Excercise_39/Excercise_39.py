################################
######### Excercise 39##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#Description:
#Working with dictionaries in Python

#Mapping multiple items to elements in a list. Each element is a key.
#Example

dict_info = {

    'States': ['Arizona', 'Masachusetts', 'California'],
    'Cities': ['Tempe', 'Boston', 'Silicon Valley'],
    'College': ['Arizona State University', 'Harvard University', 'Stanford University']
}

count = 0
for each_college in dict_info:
    information = '''
The college %s is located in %s, %s.
        ''' %(dict_info['College'][count], dict_info['Cities'][count], dict_info['States'][count])
    #College, Abbreviated State, City
    print information
    print '-' * 100
    count = count + 1

#Print out each state without using a counter

state_abbreviations = {
 #Create a mapping of relevant states with abbrviated counter-part
'Arizona': 'AZ',
'California': 'CA',
'Massachusetts': 'MA'

}

#For loop to iterate through each state to explain it's respected abbreviation
for each_state in state_abbreviations:
    format = '''
        The state %s has an abbreviation as %s.
    ''' %(each_state, state_abbreviations[each_state])
    print format
    print '-' * 100
