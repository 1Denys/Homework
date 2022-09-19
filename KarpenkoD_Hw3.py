# Exercise 1
x1 = float(input('Enter the number: '))
y1 = x1 > 0
print(y1 and 'The number is positive' or x1)

# Exercise 2
x2 = float(input('Enter the number: '))
y2 = x2 < 20
z2 = x2 > 20
print(y2 and 'Entered number is less than 20' or z2 and 'Entered number is more than 20')

# Exercise 3
x3 = float(input('Enter the number: '))
y3 = x3 == 0
print(x3 and 'number is not 0' or y3 and 'number is 0')

# Exercise 4
x4 = float(input('Enter the number: '))
y4 = bool(x4 % 2)
print(y4 and 'the number is Odd' or 'the number is Even')

# Exercise 5
s5 = tuple(input('Enter numbers'))
#s5 = 56, 87, 12
print(max(s5))
print(type(s5))
