# this is what we will use for the video intro to dictionaries

# dictionary = a collcetion of {key:value} pairs
# ordered and changeable. No Duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals)) --> prints the attribute
# print(help(capitals)) --> prints a list of things you can do to an item

# print(capitals.get("USA")) --> prints the value of the dictionary object
# print(capitals.get("India")) --> prints the value of the dictionary object

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")



#.update adds a new value or replaces existing value
# capitals.update({"Germany": "Berlin"}) 
# capitals.update({"USA": "Detroit"})
# print(capitals)

# capitals.pop("China") # removes items
# capitals.popitem #removes latest item
# capitals.clear() # clears dictionary

# prints the key of a dictionary
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

# prints every value in dictionary, could be object
values = capitals.values()

for value in capitals.values():
    print(value)

# makes it into a 2D list
items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")