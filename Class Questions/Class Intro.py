# Task :
#
# Write a program for a class Employee taking raise amount as a class variable,
# constructor to initialise first name, last name.
# Also create methods display the full name, original pay and raised pay for 2 objects


class Employee:
    raise_amount = 1000
    new_amount = 0

    def __init__(self,fname,lname,ori_pay):
        self.fname = fname
        self.lname = lname
        self.ori_pay = ori_pay

    def raised_amount(self):
        Employee.new_amount = self.ori_pay + Employee.raise_amount

    def display(self):
        print(f'Name : {self.fname} {self.lname}')
        print(f'Original Salary : {self.ori_pay}')
        print(f'Raised Salary : {Employee.new_amount}')


# Main Function

fname = input('Enter First Name : ')
lname = input('Enter Last Name : ')
ori_pay = int(input('Enter Salary : '))

obj1 = Employee(fname,lname,ori_pay)
obj1.raised_amount()
obj1.display()
