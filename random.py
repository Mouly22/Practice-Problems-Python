lst = input("Enter course code: ").split()
dict = {}
for i in range(len(lst)):
    x = lst[i]
    n = str(int(x[3])* 100) + " Level"
    #print(n)
    if n not in dict:
        lst1 = []
        lst1.append(x)
        dict[n] = lst1
    else:
        dict[n].append(x)
print(dict)