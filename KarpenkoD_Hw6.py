#Exercise 1
i = 0
while i < 100:
    print(i)
    i += 7

# Exercise 2
number = int(input('Enter the number: '))
i = 0
k = 1
while (i := i + 1) <= number:
    k *= i
print(k)

# Exercise 3
number_3 = int(input('Enter the number: '))
i = 1
while i <= number_3:
    print(f'{i} * 5 = {i * 5}')
    i += 1

# Exercise 4
a, b = 4, 5
for j in range(a):
    if j == 0 or j == a - 1:
        for i in range(b):
            print('*', end='')
        print()
    else:
        print(f"*{' ' * (b - 2)}*")

# Exericse 5
import random
x = [random.randint(1, 100) for _ in range(10)]
k = 0
for i in x:
    for digit in map(int, str(i)):
        if digit % 2:
            k += 1
print(x)
print(k)

# Exercise 6
import random
x6 = [random.randint(1, 100) for _ in range(4)]
y6 = []
y6.extend(x6)
for i in range(len(x6)):
    z = x6[i] * 2
    y6.append(z)
print(x6)
print(y6)

#variant 2
import random
x6_2 = [random.randint(1, 100) for _ in range(4)]
y6_2 = x6_2[:] + [2 * i for i in x6_2]
print(x6_2)
print(y6_2)

# Exercise 7
import random
x7 = [random.randint(5000, 7000) for _ in range(12)]
print(x7)
AVE_SALARY = sum(x7) / len(x7)
print(AVE_SALARY)

# Exercise 8
x8 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
summa = 0
for i8 in x8:
    print('\t'.join(map(str, i8)))
    summa += sum(i8)
print(summa)

#Exercise 9
x9 = list(input())
print(x9[::-1])

#Exercise 10
for n10 in range(2, 101):
    for i10 in range(2, n10):
        if not n10 % i10:
            break
    else:
        print(n10)

#Exercise 11
a11 = 5
i11 = 0
res = []
for start in range(a11, 0, -2):
    res.append(f"{' ' * i11}{'*' * start}")
    i11 += 1
res += res[-2::-1]
print('\n'.join(res))
