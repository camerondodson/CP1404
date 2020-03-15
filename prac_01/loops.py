# Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count from 0 to 100 in steps of 10
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Count from 20 to 1 in steps of 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print users selected amount of stars in one line
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# Print n lines of increasing stars
for i in range(1, number_of_stars + 1):
    print('*' * i)
