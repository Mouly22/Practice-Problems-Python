# Write the Python code of a program that reads a number,
#        and prints "The number is even" or "The number is odd", depending on whether the number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number if Odd.")



#reading from a file:
inp_file = open('input1a.txt', 'r')
out_file = open('output1a.txt', 'w')
val = inp_file.readlines()

for i in range(1, int(val[0])+1):
    store = val[i].strip()
    if int(store) % 2 == 0: 
        out_file.write(f'{store} is an Even number.\n')
    else:
        out_file.write(f'{store} is an Odd number.\n')
inp_file.close()