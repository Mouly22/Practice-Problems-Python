#Write the python programs, which prints the following sequences of values in loops:
#a) 24, 18, 12, 6, 0, -6
x = 24 
while x >= -6:
    if x == -6:
        print(x, end= " ")
    else:
        print(x, end= ", ")
    x -= 6

    
#b)-10, -5, 0, 5, 10, 15, 20
x = -10
while x <= 20:
    if x == 20:
        print(x, end= " ")
    else:
        print(x,end = ", ")
    x += 5


#d)18,-27, 36,-45,54,-63
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

