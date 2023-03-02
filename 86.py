inp1 = open('input5.txt', 'r')
out1 = open('output5.txt', 'w')
temp = inp1.readlines()
dct = {}
first_l = []
for i in range(1, len(temp)):
    varr = temp[i].split()
    name = varr[0]
    times = temp[i].strip()
    if name not in dct.keys():
        first_l.append(name)
        dct[name] = [times]
    else:
        dct[name].append(times)


def selection_asc(val_lst):
    for u in range(len(val_lst)):
        min_indx = u
        for v in range(u+1, len(val_lst)):
            if val_lst[v] < val_lst[min_indx]:
                min_indx = v
        if min_indx != u:
            temp = val_lst[u]
            val_lst[u] = val_lst[min_indx]
            val_lst[min_indx] = temp
    return val_lst

for mm in selection_asc(first_l):
    temp = None
    count = 0
    for gk in dct[mm]:
        tempgk = gk.split()
        time = tempgk[-1]
        time = time[:2]+time[3::]
        time = int(time)
        if temp == None:
            pass
        elif time > temp:
            k = dct[mm][count]
            dct[mm][count] = dct[mm][count-1]
            dct[mm][count-1] = k
        count += 1
        temp = time


for mm in selection_asc(first_l):
    for gk in dct[mm]:
        out1.write(f'{gk}\n')
inp1.close()





