# Exercise #1: (10 points)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

total = 0
for i, k in stuff.items():
    print(k, i)
    total += k
print("Total number of items : ", total)

# Exercise #2: (10 points)

characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
characters.insert(-1, 'and')
to_string = ", ".join([i for i in characters[0:6]])
to_string2 = " ".join([i for i in characters[6:]])

print(to_string, to_string2)

# Exercise #3: (10 points)

dict_one = {
    "dict": "stores a key/value pair",
    "list": "stores a value at each index",
    "map": "see dict",
    "set": "stores unordered unique elements",
    "exit": ""
}

while dict_one:
    term = input("Enter a term 'dict', 'list', 'map', or 'set' or exit ")
    if term in dict_one:
        print(dict_one[term])
        if term == "exit":
            break

#Exercise #4: (2 points)

print(sorted(set("Mississippi")))

# Exercise #5: (2 points)

list1 = [1, 2, [3, 4, "hello"]]
list1[2][2] = "goodbye"
print(list1)

# Exercise #6: (3 points)
# 6a.
d = {'simple_key': "hello"}
print(d['simple_key'])

# 6b.
d = {"k1": {"k2": "hello"}}
print(d["k1"]["k2"])
