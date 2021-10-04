# number_of_scores = int(input("Enter how may scores: "))
#
# scores = []
#
# for x in range(0,number_of_scores):
#     while True:
#         try:
#             score = int(input(f"What is the  scores {x+1}: "))
#             scores.append(score)
#         except:
#             print("Invalid score value, please try again")
#         else:
#             break

# try:
#     print(sum(scores/0))
# except:
#     print("somthing is worg")
#
# while True:
#     try:
#         email_address = input("Enter ypur email address")
#         parts = email_address.split("@")
#         name = parts[0]
#         domain= parts[1].split(".")
#         print("The email address is", name ,domain[0],domain[1])
#         print("thank you")
#         break
#     except:
#         print('The email is invalid')


def divide_by(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("number is equual to zero")
    except:
        print("invalid arguanment")

results = divide_by(1,0)
print(results)