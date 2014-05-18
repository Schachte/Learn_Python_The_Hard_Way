class MovieTracker(object):

    def __init__(self, movie, trailer, image):
        self.movie = movie
        self.trailer = trailer
        self.image = image

    def movie_name(self):
        movie = '''
Your Current Movie: %s
                ''' %(self.movie)
        return movie

    def movie_trailer(self):
        trailer = '''
The link to the movie trailer is: %s
                  ''' %(self.trailer)
        return trailer

    def movie_image(self):
        image = '''
The link to the image can be viewed: %s
                ''' %(self.image)
        return image





