import Excercise_43

employee_list = []

'''
loop = True

while (loop):
'''
object_name = raw_input('Enter name of the company employee')
employee_name = raw_input('Employee Name>>')

employee_salary = raw_input('Employee Salary>>')
employee_salary = float(employee_salary)

employee_title = raw_input('Employee Title>>')

employee_hours = raw_input('Employee Weekly Hours>>')
employee_hours = float(employee_hours)

new_emp = Excercise_43.employee(employee_name, employee_salary, employee_title, employee_hours)

employee_list.append(object_name)

print 'The Employee has been appended to the employee list'

print 'The Employee has been constructed!'

print employee_list[0].title()