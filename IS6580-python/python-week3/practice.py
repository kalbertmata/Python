# prices = [1, 2, 3, 4]
# counter = 0
# while counter <1:
#     prices[counter] *= .07
#     counter += 1
# print(prices)

# names1 = ['Jane', 'Barry', 'Kipp', 'Matt']
#
# names2 = names1
#
# names3 = names1[:]
#
# names2[0] = 'Alice'
#
# names3[1] = 'Bob'
#
# sum = 0
#
# for ls in (names1, names2, names3):
#
#     if ls[0] == 'Alice':
#
#         sum += 1
#
#     if ls[1] == 'Bob':
#
#         sum += 10
#
# print(sum)

# names1 = ['Jane', 'Barry', 'Kipp', 'Matt']
# loc = names1.index("Edward")
# print(loc)

# names1 = ['Jane', 'Barry', 'Kipp', 'Matt']
# if 'matt' in names1:
#     print(1)
# else:
#     print(2)

# numbers = [1, 2, 3, 4]
# numbers.append([5,6,7,8])
# print(len(numbers))
# print(numbers)

# a=[10,23,56,[78]]
# b=list(a)
# a[3][0]=95
# a[1]=34
# print(b)
#
# s = [['him', 'sell'], [90, 28, 43]]
#
# print(s[0][1][1])
#
# a = [1,2,3] + [4,5,6]
#
# print(a)
#
# a = ["Hi"] * 4;
#
# print(a)
#
# tot = 0
#
# for i in [5, 4, 3, 2, 1] :
#
#      tot = tot + 1
#
# print(tot)

toothpaste_list = ['Colgate','Parodontax','Sozodont']

print(toothpaste_list[-2:])

numbers = [[1,2,3],[4,5,6],[7,8,9]]
print(numbers[2][2])

a = "kalbert"

print([a])

s = "python rocks"
print(s[2] + s[-4])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[5])

print(18 / 4)
print(18 % 4)

print(16 - 2 * 5 // 3 + 1)

x = 12
x = x - 3
x = x + 5
x = x + 1
print(x)

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))

s = "python rocks"
print(s[3:8])

alist = [1,3,5]
blist = [2,4,6]
print(alist + blist)
qu = "wow, welcome week!"
ty = qu.index("k")
print(ty)

qu = "wow, welcome week! Were you wanting to go?"
ty = qu.count("we")

print(ty)

let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

s = "python rocks"
count= 0
for ch in s[3:8]:
   print("HELLO")
   count+=1
print(count)

count = 0
p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
for ch in p:
   print(ch)
   count+=1

print(count)

x = 10

if x > 0 and x < 5:
    print("good")

if (4 + 5 == 10):
    print("TRUE")
else:
    print("FALSE")
print("TRUE")

mydict = {"cat":12, "dog":6, "elephant":23}
print(mydict["dog"])

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])

def print_many(x, y):
   """Print out string x, y times."""
   for i in range(y):
       print(x)

z = 3
print_many("Greetings", z)

def cyu3(x, y, z):
   if x - y > 0:
      return y -2
   else:
      z.append(y)
      return x + 3

print(cyu3(2, 10, 4))