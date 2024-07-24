#Write a python program that prints a rectangle of size M (height/line numbers) and N (length/column numbers) using incrementing numbers 
#where M and N will be given as input. 
M = 4
N = 6
sum = ""
for i in range(N):
    sum = sum + str(i+1)
for i in range(M):
    print(sum)   

#or,
M = int(input())
N = int(input())
for x in range(M):
    for y in range(N):
        print(y+1, end = "")
    print()
