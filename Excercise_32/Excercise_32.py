'''
Storing data in lists using loops in Python
'''

#Objective:
#Build a loop that adds data into a list and then have python print the data using string formatter
'''
loop_data = [] #Instantiate an empty list to store user data in

loop_count = raw_input("Enter the number of elements you would like to iterate through in the loop:")

loop_count = float(loop_count) #Convert user string (loop_count) into a float to read numbers

count = 1 #Store the initial count to properly track the progress of the user count

while (count <= loop_count):
    loop_data.append(count)

    print 'The current element is: %d' %(count) #String format to print the user data from the list

    count = count + 1 #Increment the count by one to track the current adding progress of the data
'''

#Now we are going to do a loop with a list to store names of people in class

user_list = [] #Defining an empty user list to store user_input users into a python list

#Function to add people into a list using raw_input and lists in Python
def new_user():
    user_name = raw_input("Enter the name of the user that you would like to add into the list: ")
    user_list.append(user_name)
    print user_name + ' was appended to the list successfully!'
    return user_list


add_user = True

while (add_user == True):
    boolean_add_user = raw_input('Would you like to add a user into the class list?')
    boolean_add_user = boolean_add_user.lower()
    if boolean_add_user == 'yes':
        #If the loop is made True by user input of Yes, then call the add_user function to add another person to the list
        add_user = True
        user_list = new_user()
    elif boolean_add_user == 'no': #Exit the loop by changing the value of the boolean
        add_user = False
    else:
        print 'Please enter a valid input for the program to read!'

final_user_option = raw_input("Would you like to view the class list or exit the program? V/E")

if final_user_option == "V":
    for each_item in user_list:
        print 'The first student is: %s' %each_item
elif final_user_option == "E":
    print 'Exiting program!'










