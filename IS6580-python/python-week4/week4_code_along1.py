prices = [1.10, 0.99, 5.75]

for i in prices:
    print("Original price", i)
    i *= 107
print("Original price", prices)

# i = 0
# for item in prices:
#     prices[i] *= 1.07
#     prices[i] = format(prices[i], ".2f")
#
# print(prices)

for i in range(len(prices)):
    prices[i] *= 1.07
    print("Item price", format(prices[i], ".2f"))
print(prices)

my_number = "10 20 30 40 50 60 "

print(my_number)

number_list = my_number.split()

print(number_list)

int_list = [int(x) for x in my_number.split()]

print(int_list)

my_time= "10:05:45, 09:45:32, 07:30:25"
time_list = my_time.split(",")
for i in time_list:
    time = i.split(":")
    print(time)

time = "07:49:34"
hrs, mins, sec = time.split(":")
print(hrs, mins, sec)


