# Suppose you are given two dictionaries. Now create a new dictionary "marks", merging the two dictionaries, so that the original two dictionaries remain unchanged.
# {'Harry':15, 'Draco':8, 'Nevil':19}
# {'Ginie':18, 'Luna': 14}
# Output: {'Harry': 15, 'Draco': 8, 'Nevil': 19, 'Ginie': 18, 'Luna': 14}
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}
dict1.update(dict2)
print(dict1)