Grading = {'A':4,'A-':3.7,'B+':3.3,'B-':2.7,'B':3,'C':2,'C+':2.3,'C-':1.7,'D':1,'D+':1.3,'D-':.7,'F':0,'F+':.3}
user_input = input('Enter course number, units, and grade, separated by spaces\n')
grades = []
units = []

while user_input != '':
    data = user_input.split()
    units.append(float(data[1]))
    grades.append(data[2])
    user_input = input('Enter course number, units, and grade, separated by spaces\n')

total = 0
for i in range(len(units)):
    total += units[i] * Grading[grades[i]]

GPA = total / sum(units)
print('The GPA is {:.2f}'.format(GPA))