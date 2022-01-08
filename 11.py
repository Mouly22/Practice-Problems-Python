myDict = {}
while(True):
    x = input().split()
    if x == "STOP":
        break 
    else:
        if x not in myDict:
            myDict.update({x: 1})
        else:
            myDict[x] += 1
            
    print(myDict)

        