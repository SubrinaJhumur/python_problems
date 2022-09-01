# Calculate grade of five subjects


print('Enter your marks: ')

math = int(input('Enter the marks of math: '))
physics = int(input('Enter the marks of physics: '))
chemistry = int(input('Enter the marks of chemistry: '))
biology = int(input('Enter the marks of biology: '))
statistics = int(input('Enter the marks of statistics: '))

average = (math + physics + chemistry + biology + statistics)/5

if average >= 90:
    print('Grade: A')
elif average >= 80:
    print('Grade: B')
elif average >= 70:
    print('Grade: B')
elif average >= 60:
    print('Grade: B')
else:
    print('Grade: D')


