################################
######### Excercise 38##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################


data_list = [300, 500, 700, 8453, 2340, 235]

#List count variable to properly track the number of elements that currently exist in the data list (pre-defined values)
list_count = 0

for each_item in data_list:
    list_count = list_count + 1 #Keep track of the list count for the user to properly exit the while loop when needed


#Print statement to output the number of elements that currently exist in the users pre-defined data list
print 'There are currently %d items in the data_list. It is time to increment until the list is full with 10 integers!' %(list_count)

#Loop the following string add while the count of items in the data list is less than 10
while (list_count < 10):
    print 'Enter some data to add into the list'
    data_add = raw_input('>>')

#Append the user input to the data list
#The append will continue to loop while the number of items in the data list doesn't exceed the 10 count
    data_list.append(data_add)

    print 'Data successfully added into the list!\nData added: %s' %(data_add)

    #Increment the list count to make sure the while-loop still has the ability to exit the code
    list_count = list_count + 1

    #For each item that exists in the data list, print it out and display it to the user via the console
for each_element in data_list:
    print each_element

#Print data from data list in a specified range to exclude the final element in the console
print data_list[1:9]

print data_list

