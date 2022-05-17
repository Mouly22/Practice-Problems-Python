# Suppose you are given the following dictionary where the values are lists.
# dict = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
# Write a Python program that counts the total number of items in a dictionary’s values and prints it.
# [without using sum(), len(), count() functions]
dc = {'A': [1, 2, 3, 4, 6], 'b': ['1', '2', 3], "c": [4, 5, 6, 7]}
count = 0
for i in dc.values():
    for j in i:
        count += 1
print(count)