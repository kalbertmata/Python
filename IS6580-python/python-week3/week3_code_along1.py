empty_list= []
empty_list2 = list()
print(type(empty_list))
my_list= [95,3.2,"Marvel",17,4]
print(my_list)
print(my_list[2])

second_list = [100,101]
print("Second list", second_list)

second_list *= 2

print(second_list)
bigger_list = my_list + second_list
print(bigger_list)

characters = ['Thor', "Capitan America", "Wolverine", "Dumbledore", "Black Panther","Spider-man"]

print(characters)
print(characters[2])
print(characters[1:3])
print(characters[:-3])
print(characters[::3])
print(characters[2][-1])