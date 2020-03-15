"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A value error will occur when a non number input is used
2. When will a ZeroDivisionError occur?
    A zero division error will occur when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    By reminding the user to not divide by zero the ZeroDivisionError no longer appears
    however if the user does divide by zero for the second time the ZeroDivisionError will occur
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Do not divide by zero")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
