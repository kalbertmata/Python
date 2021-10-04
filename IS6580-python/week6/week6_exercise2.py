# #1. Divide by zero exception (5 points)
#
# def divide_by(num1,num2):
#     try:
#         return num1/num2
#     except ZeroDivisionError:
#         print("number is equual to zero")
#     except IndexError:
#         print("invalid arguanment")
#
# results = divide_by(1,1)
# print(results)
#
# # 2. Basic exception handling (5 points)
# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except:
#     print("Invalid can't raise an string to the power of any number")
#
#
#
# #3. try-except-finally (5 points)
#
# try:
#     x = 5
#     y = 0
#     z = x / y
# except ZeroDivisionError:
#     print('')
# finally:
#     print("All done")
#
# #4. try-except-else(5 points)
# def interger_func():
#
#     while True:
#
#         try:
#             interger_in = int(input("enter an integer: "))
#             x = interger_in**2
#             return "this is your number", x
#         except:
#             print("lol")
#
#
# print(interger_func())

try:
    for i in range(5):
        print(1.0 / (3-i))
except Exception as error_inst:
    print("Got an error", error_inst)