val = int(input("Enter the digit: "))
lst = []
for i in range(len(str(val))):
    if i == 0:
        ans = val% 10
        lst.append(ans)
        rem = val // 10
    if i>0:
        ans = rem % 10
        lst.append(ans)
        rem = rem // 10

for x in lst:
    if x == lst[-1]:

        print(x, end=' ')
    else: 
        print(x, end = ', ')
