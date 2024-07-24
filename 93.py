print("Take a input from the user and find out whether there exists 3 consequtive uppercase letters. If so, then print all the uppercase letters altogether, else print all the lowecase letters altogether.")

userInp = input("Enter your string: ")
count = 0
lst = []
flag = True
lst2 = []
for i in range(len(userInp)):
    if ord(userInp[i]) >= 65 and ord(userInp[i]) <= 90:
        flag = False
        
        
        count += 1
        lst.append(userInp[i])

       
        if count >= 3:
            for x in lst:
                print(x, end = '')
            
          
    else:
        count = 0
        if count < 3:
            
            if (ord(userInp[i]) >= 97 and ord(userInp[i]) <= 122):
                flag = True
                lst2.append(userInp[i])
                
if flag:
    for y in lst2:
        print(y, end = '')



        
        
