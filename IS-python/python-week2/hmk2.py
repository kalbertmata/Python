import random

# 2.1 Write a program that asks the user for the value of a coin.
# Then determine what kind of coin they entered using this information.
# Provide a message if you enter any other value that does not match.

penny = 1
nickle = 5
dime = 10
quarter = 25
half_dollar = 50
coin_value = int(input("what is the value of your coin? "))
if coin_value == penny:
    print("Your coin is a penny")
elif coin_value == nickle:
    print("Your coin is a Nickle")
elif coin_value == dime:
    print("Your coin is a Dime")
elif coin_value == quarter:
    print("Your coin is a Quarter")
elif coin_value == half_dollar:
    print("Your coin is a Half dollar")
else:
    print("This value does not match")

# 2.2 Write a program that asks the user for a number between 1 and 10 (inclusive).
# Then report to the user the following:
# If the number is even
# If the number is odd
# If the number is prime
# If the number is not prime
# Pseudo code:
# Prompt the user for a number between 1 and 10.
# If the number is less than 1 or greater than 10, print error message. end program.
# Else,
# If the number is even,
# print even.
# else, print odd.
# If the number is 2,3,5,7 print a prime message.
# else, print it's not prime.
# End program.

number = int(input("Enter the user for a number between 1 and 10 "))
if number < 1 or number > 10:
    print("Error wrong number the end")
else:
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
if number == 2 or number == 3 or number == 5 or number == 7:
    print("is also a prime number")
else:
    print("It's not a prime number")

# Exercise 2.3: (2.5 points)
# Write a program that asks the user for the price of an item they are purchasing.
# Items are eligible for a discount based on their price as follows:
# $10 or less: no discount
# Between $10 and $50: 10 % discount
# Over $50: 20 % discount
# Ensure that you don't allow the user to enter negative values or zero as a price value.
#
item_price = float(input("Enter the price of the item "))

if item_price <= 0:
    print("Zero and negative numbers are not allowed")
elif item_price <= 10:
    print("No discount")
elif item_price > 10 and item_price < 50:
    print("10% discount")
elif item_price >= 50:
    print("20% discount")

# Exercise #2.4: (2.5 points)
# Write a program that asks the user to enter a starting number (integer), ending number (integer)
# and the word "even" or "odd". Then generate a customized printout based on their input.

starting_number = int(input("Enter an staring number "))
ending_number = int(input("Enter ending number "))
even_odd = input("please enter even or odd ")

while starting_number <= ending_number:
    if even_odd == "even" and starting_number % 2 == 0:
        print(starting_number)
    if even_odd == "odd" and starting_number % 2 != 0:
        print(starting_number)

    starting_number += 1

# I did a for loop
# starting_number = int(input("Enter an staring number "))
# ending_number = int(input("Enter ending number "))
# even_odd = input("please enter even or odd ")
#
# if even_odd == "even":
#     for i in range(starting_number, ending_number + 1):
#         if i % 2 == 0:
#             print(i)
# elif even_odd == "odd":
#     for i in range(starting_number, ending_number + 1):
#         if i % 2 != 0:
#             print(i)
# else:
#     print("Please follow the instructions")

# Exercise 2.5: (3 points)
# Write a program that asks the user to enter in a number of products (as an integer).
# Then prompt the user for that number of prices and compute the total cost of all products.

product_qty = int(input("Enter the number of product "))
result = 0
i=1

while i <= product_qty:
    price = float(input("Enter price for product " + str(i)+":"))

    result+= price
    i+=1
print(result)

# I did this one using the for loop
# product_qty = int(input("Enter the number of product "))
# result = 0
#
# for i in range(1, product_qty + 1):
#     product = int(input("Enter price for product "))
#     result += product
# print(result)

# Exercise #2.6: (3 points)
# Write a simple "shopping cart" program that asks the user for a series of product prices.
# Compute sales tax (7%) on each price and print out the new price to the user.
# Next, ask the user if they want to enter another price - if they do, repeat the process.
# If not, end the program.

price = "yes"
while price == "yes":
    items = float(input("Enter item price: "))
    tax_item = items * .07
    price_item = items * 1.07
    print("Tax on this item is {:.2F} total price: {:.2f}".format(tax_item, price_item, ))
    # this way of format was to long but it works
    # print("Tax on this item is:", "{:.2f}".format(tax_item),  "total price:", "{:.2f}".format(price_item))
    price = input("More items (yes or no)")

# Exercise 2.7: (3 points)
# Modify Exercise 6 so that your program also keeps track of the total amount spent in addition to total tax due.

Items_to_enter = "yes"
total_tax_item = 0
total_price_item = 0
while Items_to_enter.lower() == "yes":
    items = int(input("Enter item price: "))
    tax_item = items * .07
    price_item = items * 1.07
    total_tax_item += tax_item
    total_price_item += price_item
    print("Tax on this item is {:.2F} total price: {:.2f}".format(tax_item, price_item, ))
    Items_to_enter = input("More items (yes or no)")
    if Items_to_enter == "no":
        print("Total amount due {:.2f}\ntotal tax due {:.2f}".format(total_price_item, total_tax_item))

# Exercise #2.8: (3 points)Z
# Write a program that continually asks the user for the answer to a simple math question (2 + 2).
# If the user answers the question correctly you should congratulate them and end the program.
# If they answer the question incorrectly you should re-prompt them until they answer correctly.


x = int(input("what number is 2 + 2: "))
# this if statement will handle when user answers right the first time
if x == 4:
    print("Congratulations you are right!")
# this loop will handle when wrong answer and until users gets it right
while x != 4:
    x = int(input("Wrong try again 2 + 2: "))
    if x == 4:
        print("Congratulations you are right!")

# Exercise 2.9: (3 points)

# Modify Exercise 8 so that your program prompts the user
# for a random addition problem instead of always asking them to answer "What is 2+2?".
# Pseudo code:
# Generate 2 random numbers, num1, num2.
# Enter while loop
# Prompt the user "what is num1 + num2" equal?
# check the answer, if the input value equals the num1 + num2 then print "Correct!"
# Else, print "Incorrect" and try again.
# End loop.


num1 = random.randint(1, 3)
num2 = random.randint(1, 3)
sum_num1_num2 = num1 + num2
check = int(input("What is the result of num1 + num2: "))
if sum_num1_num2 == check:
    print("Correct")
while sum_num1_num2 != check:
    check = int(input("Wrong try again num1 + num2: "))
    if check == sum_num1_num2:
        print("Congratulations you are right!")
