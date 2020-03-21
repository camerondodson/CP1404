numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
# This will produce 3

print(numbers[-1])
# This will produce 2

print(numbers[3])
# This will produce 1

print(numbers[:-1])
# This will produce [3, 1, 4, 1, 5, 9]

print(numbers[3:4])
# This will produce [1]

print(5 in numbers)
# This will produce True

print(7 in numbers)
# This will produce False

print("3" in numbers)
# This will produce False as there is no string called "3"

print(numbers + [6, 5, 3])
# This will produce [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Get all the elements from numbers except the first two (slice)
print(numbers[2:])

# Check if 9 is an element of numbers
print(9 in numbers)
