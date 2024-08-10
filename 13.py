#Write a python program that prints a right-angled triangle of height N using incrementing numbers where 
# N will be given as input.
# Sample Input 1:             Sample Output 1:
#       4                           1
#                                   12
#                                   123
#                                   1234
print()
inp = int(input("Enter Number: "))
for i in range(inp):
    for j in range(i+1):
        print(j+1, end = '')
    print()




















# x = 5
# st = ""
# for i in range(x):
#     st += str(i+1)
#     print(st)

    
