# Task :
#
# Write a program that uses a class Student to store the name and marks of students
# Use list to store the marks of three subjects.
# The user enters the marks and display the marks(function)
#
# The output should be in required format :
#     Anish got [88,85,10]
#     Rahul got [100,80,90]


class Student:
    def __init__(self,name,my_list):
        self.name = name
        self.my_list = my_list

    def display(self):
        print(f'{self.name} got {self.my_list}')


# Main Function

total_stu = int(input('Enter Total Students : '))
my_list = []

for i in range(total_stu):
    name = input('Enter Name : ')

    for j in range(3):
        num = int(input('Enter Marks : '))
        my_list.append(num)

    my_obj = Student(name,my_list)
    my_obj.display()
    my_list = []
