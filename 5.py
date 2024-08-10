# #Write the python programs, which prints the following sequences of values in loops:
#a) 24, 18, 12, 6, 0, -6
x = 24 
while x >= -6:
    if x == -6:
        print(x, end= " ")
    else:
        print(x, end= ", ")
    x -= 6
print()

    
#b)-10, -5, 0, 5, 10, 15, 20
x = -10
while x <= 20:
    if x == 20:
        print(x, end= " ")
    else:
        print(x,end = ", ")
    x += 5
print()

# print("Input: 18, 27, 36, 45, 54, 63")

x = 18
while x <= 63:
    if x == 63:
        print(x, end = ' ')
    else:
        print(x, end = ', ')
    x += 9
print()

#'18,-27, 36,-45,54,-63'
count = 0
val = 18
while val <= 63:
    count +=1

    if count % 2 == 0:
        if val == 63:
            print('-'+str(val), end = ' ')
        else:
            print('-'+str(val), end = ', ')

    else:
        print(val, end = ', ')
    val += 9
print()

#prev solve:
x = 18
while x <= 63:
    if x%2 ==1:
        if x == 63:
            print(-x, end =" ")
        else:
            print(-x, end= ", ")    
    else:
        print(x, end = ", ")
    x += 9
print()



