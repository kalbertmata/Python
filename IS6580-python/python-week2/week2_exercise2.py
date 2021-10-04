
# 1. Password verification (2 points)
#
# Create a password variable and assign a value to this variable. (Such as Utes!)
#
# Prompt the user to enter a password, compare the user input with your variable.
#
# Print out Access Granted or Access Denied depending if the value is true or false.

password = 1234

user= int(input("what is the password?"))

if user == password:
    print("access granted")
else:
    print("access denied")

# Set a variable for voting age to 18. Prompt a user for their age and returns whether they can vote.
# If not, indicates how many more years until they can.

voting_age = 18

age = int(input("Please enter your age"))

if age >= voting_age:
    print("you can vote")
else:
    allow_to_vote = voting_age - age
    print("You have", allow_to_vote,  "years left to vote")


# Prompt the user to enter a temperature (What is the temperature?). Use integers, assume Fahrenheit. Use the following table to print out your message:
#
# Less than 40: Wear a warm coat.
#
# Less than 70: Wear a light jacket.
#
# Less than 100: Wear something cool.
#
# 100 or greater: Prompt “Do you have air conditioning at home? (yes/no)”
#
# If yes: print: “Stay at home.”
#
# If no: print: “Bummer, try a swimming pool.”

temp = int(input("what is the temperature?"))
if temp < 40:
    print("Wear a warm coat")
elif temp <70:
    print("Wear a light jacket.")
elif temp >=100:
    promptemp= input("“Do you have air conditioning at home? (yes/no)")
    if promptemp == "yes":
        print("Stay at home.")
    else:
        print("Bummer, try a swimming pool.")







