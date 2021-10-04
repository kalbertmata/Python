
# Create a program that asks for the number of pennies, nickels, dimes, and quarters a person has.
#
# The program calculates the total and prints it to the screen with the $ sign.
# pseudocode:
# Prompt user for each coin.
# Total the sum of all values entered by user muliplying by the respective coin value.
# ex. total = nickels * .05 + ...
# format the total in currancy and print the amount of change the user has.

pennies = float(input("how many pennies do you have?"))
nickels = float(input("how many nickels do you have?"))
dimes = float(input("how many dimes do you have?"))
quarters = float(input("how many quarters do you have?"))

total = (pennies * .01) + (nickels * .05) + (dimes * .1) + (quarters * .25)

print(total, "$", "in change")

# Calculates the value of another currency in US Dollars.
#
# Prompts the user to enter the current exchange rate between the two currencies.
#
# Asks the user to enter an amount to convert.
#
# Calculates and prints out the value in US dollars, formatted to two decimal places.
#
# pseudocode:
# Prompt user for exchange rate
# Prompt user for currency amount to convert
# Calculate currency, exchange rate * amount
# Print the amount in currency format to the user

rate = float(input("what is the rate?" ))
amount = float(input("What is the amount that you want to convert?" ))
results = rate * amount

print("$", amount, "of this currency is", "$", results)
