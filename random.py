lst = []
lst2 = []
nlst = []
while(True):
    num = input()
    if num == "STOP":
        break
    else:
        num = int(num)
        lst.append(num)
        
count = 0
lst.sort()
#print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            count += 1
            
    nlst.append(count)
    count = 0

for i in range(len(lst)):
    if lst[i] != lst[i-1]:
        print(lst[i],'-',nlst[i],'times')