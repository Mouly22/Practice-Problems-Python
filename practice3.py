#adding two dict together
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}
dict1.update(dict2)
print(dict1)

#if they say dict 1 and 2 will remain unchanged, then we have to copy dict1;then we'll add dict2 with it
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}
ndict = dict1.copy()
ndict.update(dict2)
print(ndict)