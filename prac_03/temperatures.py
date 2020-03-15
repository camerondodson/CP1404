"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()


def convert_celcius_to_farhrenheit():
    fahrenheit = celsius * 9.0 / 5 + 32


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        convert_celcius_to_farhrenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit-32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

main()
