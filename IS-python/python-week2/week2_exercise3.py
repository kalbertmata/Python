# 1 Countdown (3 points)

# Asks the user for a number and then counts down by ones from that number until it gets to zero.
# Prints, "Done!" at the end.

x = int(input("enter a number"))
while x != 0:
    x -= 1
    print(x)
    if x == 0:
        print("done")

# this is a another way to do it

x = int(input("enter a number"))
while x > 0:
    x -= 1
    print(x)
print("done")

x = int(input("enter a number"))
if x > 0:
    for i in range(0, x, 1):  # I had to add the zero to the range function if I'm changing the default stepper
        x -= 1
        print(x)
    print("done")

#2 Shopping Total (3 points)

# Calculates the total including sales tax (8.875%) of a shopping trip.
# Create a total variable and a tax variable. Total the items calculated with tax.
# Be sure to test if the price is above zero.
# Continues to prompt the user to enter prices until they are done.
# Hint: enter a while loop until the user types ‘done’ at the prompt.

# Pseudo code:
# Create a few variables to hold the price of the item and the total.
# Prompt the user to enter the price of the item.
# Enter loop, while the item is not equal to "done".
# Set a new variable to the price as a float value.
# Check if the price is 0 or higher, if less than 0 prompt the user to correct the price. (Hint: use a nested 'while' loop.
# Add the price to the total variable.
# Prompt the user to enter the price of the next item.
# End loop.
# Add up the total and calculate the tax.
# Format and display the total amount to the user.
# End program.


# this is the one I did
# price_taxed = 0
# item = ""
# total = 0
#
# while item != "done":
#     price_user = float(input("Enter price:"))
#     if price_user >= 0:
#         price_taxed = price_user * 1.0887
#         total += price_taxed
#         item = input("more items yes/done ")
#         if item == "done":
#             print("the total amount is: {:.2f}".format(total))
#     else:
#         print("enter the right price")

total = 0
tax = 0.0887
item = input("Enter price:")

while item != 'done':
    price = float(item)

    while price < 0:
        price = float(input("Enter price:"))
    total += price
    item = input("Enter price:")
total = total + total * tax

total = format(total,".2f")
print("your total$", str(total))