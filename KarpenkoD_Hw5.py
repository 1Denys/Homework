# Exercise 1
number = input('Number: ')
x = list(map(int, number))
sum1, sum2 = 0, 0

if len(x) % 2 != 1:
    for i1 in range(0, len(x)//2):
        sum1 += x[i1]
    for i2 in range(len(x)//2, len(x)):
        sum2 += x[i2]
    print(sum1 == sum2 and 'Happy number' or 'Unhappy number')
else:
    print('Enter even number')

# Exercise 2
s = str(789987)
k = 0
for i1 in range(len(s)//2):
    if s[i1] != s[-i1 - 1]:
        k = 1
        break
if k == 1:
    print('not polindrom')
else:
    print('polindrom')

# Task 2.1
s = 'А роза упала на лапу Азора'
s1 = ''
k = 0
for i in range(len(s)):
    if s[i] != ' ':
        s1 += s[i]
s2 = s1.lower()

for i1 in range(len(s2)//2):
    if s2[i1] != s2[-i1 - 1]:
        k = 1
        break

if k == 1:
    print('not polindrom')
else:
    print('polindrom')

# Exercise 3
x = float(input('Enter x: '))
y = float(input('Enter y: '))

X0 = 0
Y0 = 0
RADIUS = 4
if (x - X0)**2 + (y - Y0)**2 <= RADIUS**2:
    print('Point inside of circle')
else:
    print('Point outside of circle')
