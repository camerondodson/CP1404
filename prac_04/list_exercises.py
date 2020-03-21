numbers = []

# Instructions for user
print("Please enter 5 numbers")

# Get user to input each of the 5 numbers
for number in range(1, 6):
    number = int(input("Enter number {}: ".format(number)))
    numbers.append(number)

# Find the first number
print("The first number is {}".format(numbers[0]))

# Find the last number
print("The last number is {}".format(numbers[-1]))

# Find the smallest number
print("The smallest number is {}".format(min(numbers)))

# Find the largest number
print("The largest number is {}".format(max(numbers)))

# Find the average of all 5 numbers
print("The average of the numbers is {}".format(sum(numbers)/5))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")