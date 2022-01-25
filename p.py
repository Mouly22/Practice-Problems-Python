x = 'AABAABBAA'

usr_inp = input("Enter a string: ")
dict1 = {}
for i in usr_inp:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1
print(dict1)

x = 'AABAABBAA'
y = x.count('AB')

dict = {}
while(True):
    x = input("Enter: " ) 
    if x == 'STOP':
        break 
    else:
        if x not in dict:
            dict.update({x: 1})
        else:
            dict[x] += 1
            
for x,y in dict.items():
    print(x,'-',y,'times')      




