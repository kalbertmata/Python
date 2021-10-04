# Exercise 1: (3 points)
# Given the list below, write a program that counts the
# of A’s (scores between 90 and 100). Extension: Count the # of B’s, C’s, D’s and F’s.
# Hint: use an if-elif-else condition inside a for loop.

grades = [90, 100, 70, 45, 76, 84, 93, 21, 36, 99, 100]
a = 0
b = 0
c = 0
d = 0
f = 0
for i in grades:
    if i >= 90:
        a += 1
    elif i >= 80:
        b += 1
    elif i >= 70:
        c += 1
    elif i >= 65:
        d += 1
    else:
        f += 1
print("We found {:.0f} A's in the list".format(a))
print("We found {:.0f} B's in the list".format(b))
print("We found {:.0f} C's in the list".format(c))
print("We found {:.0f} D's in the list".format(d))
print("We found {:.0f} F's in the list".format(f))

# Pseudo code: for each score in list,
# If grade is greater than or equal to 90, move on to next score.
# Else if score is greater or equal to 80 but less than 90, add 2 points.
# Else if score is greater or equal to 70 but less than 80, add 5 points.
# Else, add 8 points
# Print out the new grades.

grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
new_grades=[]
a = 0
b = 0
c = 0
d = 0
f = 0
for i in grades:
    if i >= 90:
        new_grades += [i]
    elif i >= 80:
        new_grades += [i+2]
    elif i >= 70:
        new_grades += [i+5]
    elif i >= 65:
        new_grades += [i+5]
    else:
        new_grades += [i+8]
for i in new_grades:
    if i >= 90:
        a += 1
    elif i >= 80:
        b += 1
    elif i >= 70:
        c += 1
    elif i >= 65:
        d += 1
    else:
        f += 1
print("Old grades", grades)
print("New grades", new_grades)
print("This is new grades after applying the curve {:.0f} A's".format(a))
print("This is new grades after applying the curve {:.0f} B's".format(b))
print("This is new grades after applying the curve {:.0f} C's".format(c))
print("This is new grades after applying the curve {:.0f} D's".format(d))
print("This is new grades after applying the curve {:.0f} F's".format(f))

# Exercise 3: (3 points)
#
# Write a program that asks the user for daily sales figures for a full week (Sunday – Saturday).
# Store these values in a list and print them out at the end of your program.
# Here's a sample running of your program:

weekly_sales = []
counter = 1
while counter >= 1 and counter <7:
    x = int(input(f"Enter sales for Day {counter} "))
    weekly_sales += [x]

    counter+=1
print("This is your weekly sales", weekly_sales)

# Exercise #4: (3 points)
# Given the following list, write a program that does the following:
# Extract the first 3 elements of the list into a new list
# Extract the characters b, c, and d into a new list
# Extract the last 4 characters into a new list

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
first_list = my_list[0:3]
second_list = my_list[1:4]
third_list = my_list[-4:]

print(first_list)
print(second_list)
print(third_list)

# Exercise #5: (3 points)
# Given the following lists, write a program that lets the user type in the name of a product.
# If the product name exists in our inventory, you should print out that it is in our inventory.
# Otherwise you should print out that the product is not found. Ensure that your program is case insensitive
# (i.e. searches for "Apple" or "apple" or "APPLE" should all succeed).

products = ["apple", "pear", "peach", "banana"]
name_product = input("Enter product name: ").lower()

for i in products:
    if name_product == i:
        print("The product is in our inventory")
    elif name_product not in products:
        print("Product is not found")
        break
    elif name_product != i:
         i += name_product
         break
#Exercise #6: (3 points)

# Given these two lists, write a program that finds all elements that exist in both lists
# (i.e. the integer 2 exists in both lists). Store your results in a list and print it out to the user.
# The expected answer is:

a = [1, 2, 3, 4, 5]
b = [2, 3, 10, 11, 12, 1]
match_a_b = []
for i in a:
    for j in b:
        if i == j:
            match_a_b += [j]
print(match_a_b)

# Exercise #7: (3 points)
# Write a program that continually prompts a user to enter in a series of first names.
# The user can elect to stop entering names when they supply the string "end."
# Store these first names in a list and print them out at the end of your program. Extension:
# Prevent the user from entering duplicate names (hint: use the in operator).


counter = 1
names_list = []
while counter == 1:
    names = input("Enter first names, to stop the program enter end:")
    if names == "end":
        counter = 0
    for i in names_list:
        if i == names:
            print(f"Name {i} is duplicated")
            #del names_list[-1] I added the delete outside the loop so it could also handle the del of "end"
            counter = 0
    else:
        names_list += [names]

del names_list[-1]
print(names_list)

# Exercise #8: (3 points)
# Continually ask the user for a product name. Next, see if that product name is included in the inventory list below.
# If it is, remove the product from the list and then print the current list of products to the user.
# If the product is not on the list you should alert the user that we do not currently carry the product in question.
# You can end the program when the list of products is exhausted or when the user types the string "end."

products = ["apple", "pear", "peach", "banana"]
counter = 1

while counter == 1:
    name_product = input("Enter product name: ").lower()
    if name_product in products:
        products.remove(name_product)
        if not products:
            counter = 0
    else:
        print("not found")
        break
print(products)

# Exercise #9: (3 points)
# The lists below are organized in such a way that the item at position 0 in the first list matches with
# the item at position 0 in the second list. With this in mind, write a product price lookup program that works
# as follows:

products = ['peanut butter', 'jelly', 'bread']

prices = [3.99, 2.99, 1.99]

check_out = input("Enter a product form the list: ")

for i in products:
    #for j in prices:
    if check_out in products:
        for j in prices:
            if products.index(check_out) == prices.index(j):
                break
print("This product costs ", j)

# Exercise #10: (3 points)

# Write a program that asks a teacher for the number of students in his or her class.
# Next, ask the teacher how many assignments are given in this class.
# With this information prompt the user to enter in scores for each student and
# compute their average grade in the class.

# Hint: use a nested for loop for the assignments inside the student for loop.
# (For each student, iterate for each assignment)

students = int(input("How many students in the class? "))
classes = int(input("How many assignments in the class? "))

scores_total = 0
avg_score = 0

i = 0

for i in range(students):
    print("Students #", i + 1)
    for j in range(classes):
        #print("Students #", i+1)
        scores_per_class = int(input(f"Assignment # {j+1}: "))
        scores_total += scores_per_class
    print("Student #", i+1, "Earned a ", scores_total / classes)

        #for j in classes:



