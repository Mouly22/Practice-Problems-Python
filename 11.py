inp_file = open('input1a.txt', 'r')
out_file = open('output1a.txt', 'w')
val = inp_file.readlines()

for i in range(1, int(val[0])+1):
    store = val[i].strip()
    if int(store) % 2 == 0: 
        out_file.write(f'{store} is an Even number.\n')
    else:
        out_file.write(f'{store} is an Odd number.\n')
inp_file.close()