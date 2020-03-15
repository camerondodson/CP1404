# Gather user input information on how many items are purchased
# Gather user information on the price of each item
# If total is greater than $100 apply 10% discount
# Display the total price of all items
total = 0
number_of_items = int(input("Number of items purchased: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items purchased: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for ", number_of_items, " items is $", total, sep='')