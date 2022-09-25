# Exercise 1
FLOORS = 9
FLAT_IN_FLOOR = 4
NUMBER_OF_ENTRANCE = 4

flat = int(input('flat number: '))
if 0 < flat <= FLOORS * FLAT_IN_FLOOR * NUMBER_OF_ENTRANCE:
    entrance = (flat - 1) // (FLAT_IN_FLOOR * FLOORS) + 1
    floor = (flat - 1) // FLAT_IN_FLOOR - (entrance - 1) * FLOORS + 1
    fl_number = (flat - 1) % FLAT_IN_FLOOR + 1
    print(flat, entrance, floor, fl_number)
else:
    print('Wrong number of flat')

# Exercise 2
year = 2022
if year % 4 == 0:
    print('leap year, number of days equals 366')
elif year % 100 != 0:
    print('not leap year, number of days equals 365')
elif year % 400 == 0:
    print('leap year, number of days equals 366')
else:
    print('not leap year, number of days equals 365')
# variant 2
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('leap year, number of days equals 366')
else:
    print('not leap year, number of days equals 365')

# Exercise 3
a = 3
b = 4
c = 5
if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
else:
    print("Triangle doesn't exist")
