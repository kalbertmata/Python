import random


def topOrBottom():
    return "#####"


def left_right():
   return "#   #"


def middle():
    return " ## "


def center():
    return " #"


print(topOrBottom())
print(left_right())
print(middle())
print(center())
print(middle())
print(left_right())
print(topOrBottom())

# Exercise #2: (5 points)


def ft_inches(ft_i):
    ft_in = ft_i * 12
    return ft_in


def ft_meter(ft_m):
    ft_me = ft_m * 0.3048
    return ft_me


for i in range(10):
    print(f"{i} ft")
    print("...", ft_inches(i), "inches")
    print("... {:.4f} meters".format(ft_meter(i)))


# Exercise #3: (5 points)

def dice_func(dice=5):
    dice1_roll = random.randint(1, dice)
    dice2_roll = random.randint(1, dice)
    return dice1_roll, "&", dice2_roll


def roll_func(time=5):
    for t in range(time):
        print(f"{t+1} sided dice roll:", dice_func(5))


roll_func(5)

# Exercise #4: (5 points)
print('I am thinking of a number between 1 and 20.')
num_user = int(input("Take a guess.\n"))
secret_number = random.randint(1, 20)
guesses = 1
print(secret_number)
# Ask the player to guess 6 times.
for g in range(1, 7):
    if num_user == secret_number:
        print(f"Good job! You guessed my number in {guesses} guesses!")
        break
    elif num_user != secret_number:
        if num_user > secret_number:
            print("number is too high")
            guesses += 1
            num_user = int(input("Take a guess.\n"))

        else:
            print("number is too low")
            guesses += 1
            num_user = int(input("Take a guess.\n"))
            if guesses == 6:
                print(f"Nope. The number I was thinking of was {secret_number}")
        