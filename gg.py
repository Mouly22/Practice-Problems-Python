lst = input("Enter a list: ").split(", ")
dict = {}
count = 0
for i in range(len(lst)):
    count += 1
    level = lst[i]
    p = str(count) +"_"+level[0:2]+"_"+level[-1:-5]
    if level not in dict:
        nlst = []
        nlst.append(p)
        dict[level] = nlst
        
    else:
        dict[level].append(p)
print(dict)