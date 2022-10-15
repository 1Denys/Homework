#Exercise 1
i = int(input('Enter the number: '))
dict_one = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
print(i, dict_one[i])

#Exercise 2
cat = {
        "name": "Lucky",
        "lastname": "Tfd",
        "breed": "British",
        "age": "2 years"}
print(cat)

#Exercise 3
s = 'Hello world'
res = {}
for i in s:
    if res.get(i):
        res[i] += 1
    else:
        res[i] = 1
print(res)

#Exercise 4
money = 123.34
money_1 = str(money)
print(money_1[1])
number = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}
for i in money_1:
    if money >= 100:
        print(number.get(money_1[map(int, i)]))
print(number.get(money_1[1]), number.get(money_1[2]))

