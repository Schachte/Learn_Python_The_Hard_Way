################################
######### Excercise 41##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################
import Excercise_41Ext
import webbrowser

movie_panel = []

def get_movie_information():
    movie_name = raw_input('Movie Name >>')
    movie_url = raw_input('Movie URL >>')
    movie_image = raw_input('Movie Image >>')

    movie_panel.append(Excercise_41Ext.MovieTracker(movie_name, movie_url, movie_image))
    print 'Data Appended'

get_movie_information()

continue_looping = True


while continue_looping:

    print 'Would you like to add another movie database?'
    continue_loop = raw_input('>>')

    if "yes" in continue_loop:
        get_movie_information()

    elif 'no' in continue_loop or 'No' in continue_loop or 'N' in continue_loop:
        continue_looping = False
        break

    else:
        print 'Please enter a valid program input'

print 'Displaying Each Movie Name From The Movie List!'

print 'Enter which trailer you would like to play for each movie!'

counter = 0

for each_item in movie_panel:
    print str(counter) + ")" + each_item.movie
    counter = counter + 1

movie_number_selection = raw_input('>>')

movie_number_selection = float(movie_number_selection)

new_counter = 0

#Pull up movie URL based ont he user integer input to pull up the movie information form the list.
#Make a while loop that displays the data based ont he number matching with the movie name

while (new_counter < movie_number_selection):
    new_counter = new_counter + 1
    print 'Counter Incremeneted to match the designated number matching with the movie'

print movie_panel[new_counter].trailer
print 'Opening movie trailer for the specified movie:'
webbrowser.open_new(movie_panel[new_counter].trailer)