################################
######### Excercise 36##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

#Description:
#Debugging & Designing Programs

#Goal is to finalize a function navigation game
life_count = 3
coin_count = 0

print 'Name?'
name = raw_input('>>')

def rm1():
    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:
        print 'Yikes, you were eaten by a monster! Your life count is currently %d and you have been sent back to entry'
        life_count = life_count - 1
        entry_point()

def rm2():
    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:
        print 'Congrats, you have gained a coin!'
        coin_count = coin_count + 1
        print 'Your current coin count is at %d' %(coin_count)

        print 'You are now able to access the following!'
        print '''
        Room 4)
        Room 5)
        Room 6)
        '''

        room_choice = raw_input(">>")

        if '4' in room_choice:
            rm4()
        elif '5' in room_choice:
            rm5()
        elif '6' in room_choice:
            rm6()
        else:
            print 'Please enter a valid input for the program to interpret'

def rm3():

    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:

def rm4():

    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:
        print 'Congrats, you have gained a coin!'
        coin_count = coin_count + 1
        print 'Your current coin count is at %d' %(coin_count)

        print 'You are now able to access the following!'
        print '''
        Room 7)
        Room 8)
        Room 9)
        '''

        room_choice = raw_input(">>")

        if '7' in room_choice:
            rm7()
        elif '8' in room_choice:
            rm8()
        elif '9' in room_choice:
            rm9()
        else:
            print 'Please enter a valid input for the program to interpret'


def rm5():
    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:


def rm6():

    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:


def rm7():
    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:


def rm8():
    if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:


def rm9():
        if life_count <= 0:
        print 'Sorry, you have run out of lives! GAME OVER!'
    else:


def entry_return():
    print 'Sorry for your loss!'
    print '''
    At this point, being in the entry room, you can access\n
    Room 1)
    Room 2)
    Room 3)
    '''
    room_choice = raw_input(">>")
    room_choice = room_choice.lower()

    if '1' in room_choice or 'one' in room_choice:
        rm1()
    elif '2' in room_choice or 'two' in room_choice:
        rm2()
    elif '3' in room_choice or 'three' in room_choice:
        rm3()
    else:
        print '''
            Sorry, that input is not valid.
            You can only enter the next 3 rooms at a single time.
              '''

def entry_point():
    welcome_message = '''
    Hello, %s! You are currently in the entry room of the game.
    There are 10 total rooms, with the 10th room being the winning locations.
    You can only access the next 3 rooms at a time.
    At this point, being in the entry room, you can access\n
    Room 1)
    Room 2)
    Room 3)
    '''
    room_choice = raw_input(">>")
    room_choice = room_choice.lower()

    if '1' in room_choice or 'one' in room_choice:
        rm1()
    elif '2' in room_choice or 'two' in room_choice:
        rm2()
    elif '3' in room_choice or 'three' in room_choice:
        rm3()
    else:
        print '''
            Sorry, that input is not valid.
            You can only enter the next 3 rooms at a single time.
              '''
def opening_message():

    print '''
    Ok, %s. Here is the objective of the game:
    You need to reach the end of the castle with at least 5 coins.
    Only four of the available rooms contain coins.
    In order to reach the required amount of coins, you must have a streak of navigation greater than 1.
    If you hit a room with a monster, your life decrements by 1. (You have 3 lives)
    If you have a streak navigation to a room greater than one, then you earn 2 coins instead of 1.
    '''
