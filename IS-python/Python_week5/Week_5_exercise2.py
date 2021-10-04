
# 2.1. Sum of numbers (3 points)

def numbers_function(number):
    add_number = 0
    for i in number:
        add_number += i
    return add_number


print(numbers_function([1, 2, 4, 3]))

# 2.1. Sum of numbers (3 points)

def power_func(a, b):
    return a**b

x = power_func(2, 2)

print(x)

#2.3. Tax function (3 points)


def tax_items(price):
    tax = price * 1.07
    return format(tax, ".2f")


price= int(input("enter price"))
y = tax_items(price)
print(y)

#2.4. Average function (3 points)

def average(n1, n2, n3):

    sum = n1 + n2 + n3
    avg = sum/3
    return avg


print(average(5, 15, 5))






