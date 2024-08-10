print('''Write a python program that prints a rectangle of size M (height/line numbers) and N (length/column numbers)
       using incrementing numbers where M and N will be given as input. 
       Sample Input 1:
        4
        6
       Sample Output 1:
       123456
       123456
       123456
       123456
      ''')

M= int(input("Enter Column Number: "))
N = int(input("enter Row Number: "))
for x in range(M):
    for y in range(1, N+1):
        print(y, end = '')
    print()
 











