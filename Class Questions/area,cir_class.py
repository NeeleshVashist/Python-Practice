# Task :
#
# Create a class Circle using class variable constant_pie.
# Use the class variable to calculate the area and circumference with a specified
# radius entered by the user.

class Circle:
    constant_pie = 3.14

    def __init__(self,radius):
        self.radius = radius

    def display(self):
        area = radius**2 * Circle.constant_pie
        circumference = 2 * Circle.constant_pie * radius

        print(f'Area : {area}')
        print(f'Circumference : {circumference}')


# Main Function

radius = float(input('Enter Radius : '))

my_obj = Circle(radius)
my_obj.display()
