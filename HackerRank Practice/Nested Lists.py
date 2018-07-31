# Task :
#
# Given the names and grades for each student in a Physics class of  students,
# store them in a nested list and print the name(s) of any student(s) having the
# second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names
# alphabetically and print each name on a new line.

N = int(input())

students = list()
for i in range(N):
    students.append([input(), float(input())])

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print(s)
