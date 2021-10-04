my_dict = {
    "name": "Thor",
    "age": 25,
}
print(my_dict)

example_dict = {
    "animals": ["dog", "cat", "fish"],
    "number": 1,
    "a_name": "Odin",
    "a_boolean": True,
    "another_dict:":{
        "you could": "Keep going",
        "like this": "forever"
    }
}

for key in example_dict:
    print(key)

for i in example_dict.items():
    print(i)
for key in example_dict:
    print(example_dict[key])

for key in example_dict.keys():
    print(key)
seasons = {
    "Fall": ["September","october","November"],
    "spring": ["March","April","May"],
    "Summer":["June","July","August"]
}

print(seasons)
winter_season = {
    "Winter": ["December","January","fabuary"]

}

seasons.update(winter_season)
print(seasons)

for key, value in seasons.items():
    print(key, value)
#sets
small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)
print(small_primes)

print( 3 in small_primes)
print( 4 in small_primes)
print( 4 not in small_primes)

# tuples
t = "a", "b", "c", "d"
print(t)
#t[1]= "xyz"
print(type(t))
