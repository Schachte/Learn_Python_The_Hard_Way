class CarDetails(object):

    def __init__(self,carname, type, mpg, color):
        self.carname = carname
        self.type = type
        self.mpg = mpg
        self.color = color

    def names(self):
        return 'Owner: %s' %(self.carname)

    def car_type(self):
        return 'Car type: %s' %(self.type)

    def miles_per(self):
        return 'MPG: %s' %(self.mpg)

    def color_type(self):
        return 'Car color: %s' %(self.color)
