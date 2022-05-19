# Suppose there is a dictionary named my_dictionary.
# my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}.
#write a Python program to remove empty items from the dictionary. [Empty items means keys without any values (None)].
#Output: {'c1':'Red', 'c2':'Green', 'd4':'Blue'}
ary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
d = {}
for i,j in ary.items():
    if j != None:
        d[i] = j
print(d)