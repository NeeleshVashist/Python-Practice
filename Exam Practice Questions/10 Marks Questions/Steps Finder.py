# Task :
#
# A robot moves in a plane starting from the origin point (0,0).
# The robot can move up, down, left and right with a given steps.
# The trace of the robot movement is shown as
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# the number after the direction are the steps
#
# WAP to compute the distance from the current position after a sequence of movement
# at the original point. If the distance is float then just print the nearest int
#
# Sample Input :
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# Sample Output :
# 2

print("Enter the Coordinates")
for i in range (4):
    a=input("Enter the Movement: ").split()
    b=int(a[1])

    if (a[0]=='UP'):
        up=b
    if (a[0]=='DOWN'):
        down=b
    if (a[0]=='LEFT'):
        left=b
    if (a[0]=='RIGHT'):
        right=b

if (up>down):
    a=up-down
else:
    a=down-up
if  (left>right):
    b=left-right
else:
    b=right-left

distance= (a*a+b*b)**0.5
print(int(distance))
