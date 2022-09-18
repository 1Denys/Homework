# Exercise 1
a1 = '123'
b1 = int(a1)
print(type(a1))
print(type(b1))

# Exercise 2
a2 = 123
b2 = float(a2)
print(type(a2))
print(type(b2))

# Exercise 3
a3 = 12.345
b3 = int(a3)
print(type(a3))
print(type(b3))

# Exercise 4
c_card = '1234 5678 1478 9632'
print(c_card[(len(c_card) - 4):len(c_card)])

# Exercise 5
a5 = 123
#y1 = int(str(a5)[0])
#y2 = int(str(a5)[1])
#y3 = int(str(a5)[2])
#sum = y1 + y2 + y3
b5 = a5 // 10
c5 = b5 // 10
d5 = b5 % 10
e5 = a5 % 10
sum = c5 + d5 + e5
print(sum)

# Exercise 6
a6 = 5
b6 = 6
c6 = 7
p2 = (a6 + b6 + c6) / 2
area = (p2 * (p2 - a6) * (p2 - b6) * (p2 - c6)) ** 0.5
print(area)

# Exercise 7


# Exercise 8
a8 = 123456
print(len(str(a8)))

# Exercise 9
a9 = 123456
b9 = str(a9)
print(b9[::-1])
