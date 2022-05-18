# Suppose you have been given the following list of tuples.
# list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
# Write a Python program that converts this list of tuples into a dictionary and then prints the dictionary.
# [You are not allowed to use set]
# Output:
# {'a': [1, 3, 2], 'b': [2, 1], 'c': [1]}

st = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dct = {}
for i in st:
    if i[0] not in dct:
        dct[i[0]] =[i[1]]
    else:
        dct[i[0]].append(i[1])
print(dct)