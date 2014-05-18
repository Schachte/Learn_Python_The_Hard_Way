################################
######### Excercise 40##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
Using modules, functions and classes in Python to create better program and control flow
'''
import CarInformation

car_list = []

loop = True

while (loop):
    print '''

    A) Build A Car
    B) View Car Information
    C) View Car List
    D) Exit

    '''

    choice = raw_input(">>")

    if 'A' in choice or 'a' in choice:
        car_name = raw_input('Enter Car Name: ')
        user_name = car_name
        car_type = raw_input('Enter Car Type: ')
        mpg      = raw_input('Enter MPG: ')
        color    = raw_input('Enter Car Color')

        car_name = CarInformation.CarDetails(car_name, car_type, mpg, color)

        car_list.append(car_name)

        print '"%s\'s" Car Has Been Created!' %(user_name)
    elif 'B' in choice or 'b' in choice:
        print 'Which car would you like to gain information about?'

        for each_car in car_list:
            print each_car.names()

        option = raw_input('>>')

        for each_car in car_list:
            if option in str(each_car):
                print each_car.names()
                print each_car.car_type()
            else:
                print 'Non Exist'

    elif 'C' in choice or 'c' in choice:
        for each_car in car_list:
            print each_car.names()


