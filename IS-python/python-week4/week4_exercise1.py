#4.1. Split Number List (2.5 points)

new_string = '10 67 123 46 20 18 36 250'

print(new_string.split(" "))

#4.2 Split Data into List (2.5 points)

a_string = "90 67 87 102 77 80"

another_list = a_string.split()
print(another_list)
in_list = [int(x) for x in a_string.split()]
print(sum(in_list))

#4.3 Slice Lists (2.5 points)

l = [1,2,3,4,5,6,7,8,9]
print(l[4:])

#4.4 Slice Lists with Increment (2.5 points)
b = ['a','b','c','d','e','f','g']
print(b[0::2])

