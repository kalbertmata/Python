# 1. Name function (5 points)

def fullname():
    name = input("Enter your first name: ")
    middle = input("Enter your middle initial: ")
    last = input("Enter your last name: ")
    f_name = f"{name} {middle} {last}"

    return f_name.title()

print(fullname())

# 2. String function practice (5 points)

print('Welcome to O\'Neil\'s Boat Rentals!')


welcome = "Hello there!\nHow are you?\nI'm doing fine."

print(welcome)

python = "hello python"
print(python.upper())

while True:
    age_uno = input("Enter your age: ")
    if age_uno.isdecimal():
        print(f"your age is {age_uno} ")
        break
    else:
        "Please enter a decimal"

name = "*Kalbert Mata*"

print("{:.25s}".format(name))


