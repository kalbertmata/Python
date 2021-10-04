# Part 1
print(True)
print(1==1)
print(1==2)
print(1!=1)
print(1<2)
print(1>2and 2<5)
print(1>2 or 2<5)
print(not 1>2 and 2<5)

# part 2 conditions also is call the control flow
# one way if condition

x= 5
if x > 0:
    print("x is positive")
else:
    print("x is less than 0")
print("this line will always print")

x = -1

if x>0:
    print("x is positive")
elif x==0:
    print("x is cero")
else:
    print("x is less than cero")

# Nested condition

x= 0
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is an even number")
    else:
        print("x is an odd number")
else:
    print("x is not a positive number")