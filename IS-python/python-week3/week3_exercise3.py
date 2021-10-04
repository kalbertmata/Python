#3.1 Input with a for-loop (4.5 points)
number = int(input("How many number to add "))

total = 0

for i in range(number):
    adding_number = int(input("Enter a number to add "))
    total += adding_number
print(total)

#3.2 Find the vowels – for loop (4.5 points)

phrase = input("Enter a word ")

total= 0

for i in phrase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        total += 1
print(total)