import random


num1 = random.randint(0,50)
num2 = random.randint(0,50)

answer = int(input("What is the sum of " + str(num1) + "+" + str(num2) + ": "))

num_sum = num1 + num2
if answer == num_sum:
    print("Correct")
while answer != num_sum:
    print("Incorrect")
    answer = int(input("What is the sum of " + str(num1) + "+" + str(num2) + ": "))
    if answer == num_sum:
        print("Correct")

