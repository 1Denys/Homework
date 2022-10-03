# Exercise 1
text = "ldkkfbb pkd dufn bktbl hbl"
k1 = 0
for i1 in text:
    if i1 == 'b':
        k1 += 1
print(k1)

# Exercise 2
#text2 = "Alexsa1ndr"
#for i in text2:
#    if i.istitle():
#        print('valid name')
#    elif i.isdigit():
#        #print('Not valid name')
#        break
#print('not valid name')

# Exercise 4
import math
for i4 in range(2, 12):
    text = 'Pi = {:.{k4}f}'.format(math.pi, k4 = i4)
    print(i4 - 1, text)

#Exercise 5
text5 = 'bgbfg bgbfbg bgbffdd bfddeghhgfv bgnh vf rtbrrrbvc'
text_part = text5.split(' ')
z5 = []
for i5 in text_part:
    z5.append(len(i5))
print(text_part[z5.index(max(z5))])
