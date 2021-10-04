my_list = ["Christine", "Claudia", "Renne", "Jeff"]
my_list.append("Jeff")
print(my_list)

del my_list[1]
print(my_list)

# my_list = [4, 3, 5]
# item = my_list.pop(1)
# print(my_list)

my_list.reverse()
print(my_list)

location = my_list.index("Jeff")
print(location)

prices = [3.99, 2.99, 1.99, 49.98, 0.99, 0.99]
biggest_num = max(prices)
smallest_num = min(prices)
print(smallest_num, "up to", biggest_num)

prices.insert(1, 6.99)
prices.remove(0.99)
prices.sort()
print(prices)
prices.sort(reverse=True)
print(prices)




