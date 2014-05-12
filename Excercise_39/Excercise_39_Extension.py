#########################################
######### Excercise 39 Extension#########
# Learning Python The Hard Way###########
####### Ryan Schachte ###################
#########################################


print 'Hello, welcome to the virtual super market!'

#Item with relevant pricing
market_items = {

    'Apples': '$3.17',
    'Bananas': '$2.81',
    'Peaches': '$1.22'

}

market_stock = {

    'Apples': 20,
    'Bananas': 10,
    'Peaches': 5

}

fruits = ['Apples', 'Bananas', 'Peaches']
#Iterate through each element in the two dictionaries without using a counter or a directly stated statement

for each_fruit in fruits:
    print 'There are ' + str(market_stock[each_fruit]) + ' ' +  each_fruit + ' which cost ' + market_items[each_fruit] + ' per pound.'