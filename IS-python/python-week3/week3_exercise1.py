#1.1. Color List (2.5 points)
#
# Create a basic list called colors containing the names of six colors.
# Using the print() function, print out each of the following: the entire colors variable (not in a loop),
# he length, index 4, a range from 1 to 5, a range from -3 and on, multiply colors by 2.

# pseudo code:
# create a variable list of color names called colors.
# print the list.
# print the length
# print index 4
# print an index from 1 to 5 (using slice)
# print an index from -3 (using slice)
# print(colors * 2)

colors = ["blue","green","red","white","black","brown"]
print(colors)
print(len(colors))
print(colors[4])
print(colors[0:5])
print(colors[:-3])
print(colors * 2)

#1.2. Color List Mutation (2.5 points)

#Using the same list as exercise #1.1 and using print statements for each:
# change the color name in element 5, set element 2 to equal element 4,
# create a new color list and set three more color names then concatenate the two lists together,
# set element 5 to equal your variable colors.

colors = ["blue","green","red","white","black","brown"]
print(colors)
colors[4] = "indigo"
print(colors)
colors[1] = colors[3]
print(colors)

new_color= ["orange","pink","purple"]
two_list = colors + new_color
print(two_list)

two_list[4]= colors[:]

print(two_list)