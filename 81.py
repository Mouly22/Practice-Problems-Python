inp_v = open('input1b.txt', 'r')
out_v = open('output1b.txt', 'w')
vals = inp_v.readlines()
for i in range(1, int(vals[0])+1):
    elem = vals[i].strip()
    a = int(elem[10:12])
    b = int(elem[14:17])
    opr = elem[12:14].strip()
    if opr == '+':
        res = a + b
    elif opr == '-':
        res = a - b
    elif opr == '*':
        res = a * b
    elif opr == '/':
        res = a / b
    out_v.write(f'The result of {a} {opr} {b} is {res}\n')
inp_v.close()
out_v.close()