'''
Program to parse and list employee data for FORTUNE 500 company
'''

class employee():

    def __init__(self, name, salary, title, weekly_hours):
        self.name = name
        self.salary = salary
        self.title = title
        self.hours = weekly_hours

        print 'New Employee Constructed!'

    def salary(self):
        name = self.name
        salary = self.salary

        return 'The employee %s has a yearly salary of %d' %(name, salary)

    def job_title(self):
        name = self.name
        title = self.title

        return '%s is a %s' %(name, title)

    def weekly_hours(self):
        name = self.name
        hours = self.hours

        return '%s works about %d hours per week' %(name, hours)


#class hobbies():