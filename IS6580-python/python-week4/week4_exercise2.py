#1.1 Create Dictionaries (2.5 points)

dict_one= {"name": "Kalbert", "age":12 }

print(dict_one["name"])
print(dict_one["age"])

#1.2 Update Dictionaries (2.5 points)

dict_one["age"] = "06/06/1980."
print(dict_one["age"])

#1.3 Dictionary With Lists (2.5 points)

seasons = {
    "Fall": ["September","october","November"],
    "spring": ["March","April","May"],
    "Summer":["June","July","August"]
}

print(seasons["Fall"])

#1.4 Dictionary Merge (2.5 points)

winter_season = {
    "Winter": ["December","January","fabuary"]

}

seasons.update(winter_season)
print(seasons)