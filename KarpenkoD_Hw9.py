# Exercise 1
s1 = 'mimionggjkidmfvsf bkdmbfmbd '
s2 = 'jgiudhui vjsughu usuivdfi'
set_1 = set(s1)
set_2 = set(s2)
s3 = set_1.intersection(set_2)
print(s3)

# Exercise 2
def max_1(a, b):
    for i in range(a, b):
        if not i % 3:
            str_1.append(i)
    for i in range(a, b):
        if not i % 5:
            str_2.append(i)
    s3 = list(set(str_1).intersection(set(str_2)))
    return max(s3)

str_1 = []
str_2 = []
print(max_1(1, 50))

# Exercise 4
def concotenation(a, b, c):
    d = str(a + b)
    e = d + c
    return e
print(concotenation(3, 5, 'bdbtnnb'))

# Exercise 5
def rectangle(a, b):
    for i in range(a):
        if i == 0 or i == a - 1:
            for j in range(b):
                print('*', end='')
            print()
        else:
            print(f"*{' ' * (b - 2)}*")
    return
print(rectangle(4, 5))

# Exercise 6
x = [74, 85, 32, 8, 96, 14, 32, 32, 96]
def search(seq, value):
    y = []
    for index, i in enumerate(seq):
        if i == value:
            y.append(index)
    return y

#print(search(x, 32))

# Exercise 7
def count_words(text):
    text = text.split()
    return len(text)

def count_words1(text1):
    return text1.count(' ') + 1

text7 = 'bdfbd bdfbfb dvsv ddsv vsvf ooj'
print(count_words(text7))
print(count_words1(text7))

