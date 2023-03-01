inpf = open('input4.txt', 'r')
outf = open('output4.txt', 'w')
val1 = inpf.readlines()
id = val1[1].split()
marks = val1[2].split()
num_lst = []
val_lst = []
dct = {}
for i in range(len(marks)):
    if int(marks[i]) not in dct.keys():
        num_lst.append(int(marks[i]))
        val_lst.append(int(id[i]))
        dct[int(marks[i])] = [id[i]]
    else:
        dct[int(marks[i])].append(id[i])
        val_lst.append(int(id[i]))

#for descending
for p in range(len(num_lst)):
    max_indx = p
    for q in range(p+1, len(num_lst)):
        if num_lst[q] > num_lst[max_indx]:
            max_indx = q
    if max_indx != p:
        temp = num_lst[p]
        num_lst[p] = num_lst[max_indx]
        num_lst[max_indx] = temp

#for ascending
def selection(val_lst):
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


for k in num_lst:
    for l in selection(dct[k]):
        outf.write(f'ID {l} Mark: {k}\n')
inpf.close()



