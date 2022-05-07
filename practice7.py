#**** 
#1)Write a Python program which takes a number and prints the digits from the unit place, then the tenth, then hundredth, etc. (Right to Left)
#[Consider the input number to be an INTEGER. You are not allowed to use String indexing for solving this task]
#Example: If the user gives 32768, then print 8, 6, 7, 2, 3
#Solve: using for loop 
x = input("Please enter a number: ") 
xx = int(x)
for i in x:
    y = xx % 10 
    xx = xx // 10
    if xx == 0:
        print(y, end = " ")  
    else:
        print(y, end = ", ")
#solve: using while loop 
x = 32768 
while x:
    print(x%10)
    x //= 10


#2)Write a Python program that takes a number and prints how many digits are in that number. [Consider the input number to be an INTEGER.] [You are not allowed to use len() function]
#Example: If the user gives 9876, your program should print 4.
#solve: while loop
x = int(input("enter:"))
y = 0
while x:
    x = x//10
    y = y + 1
print(y)
#solve: for loop
x = input("Enter: ")
xx = int(x)
y = 0
for i in x:
    xx = xx// 10
    y = y + 1 
print(y)

#3)** Write a Python program that takes a number from the user and prints its digits from left to right. [Consider the input number to be an INTEGER. You are not allowed to use String indexing for solving this task]
#Example: if the user gives 32768, then print 3, 2, 7, 6, 8
#solve: using for loop
y = input("Enter:")
yy = int(y)
ylen = len(y)
q = 10 ** (ylen - 1)
for i in y:
    z = yy // q
    yy = yy % q
    q = q // 10
    if yy == 0:
        print(z, end = " ")
    else:
        print(z, end = ", ")
#solve: using while loop
y = int(input("enter:"))
p = 0                       #p is the counter for counting the increment of y
s = 0                       #s is the counter for counting the decrement of q 
z = y
while y:
    y = y // 10 
    p += 1
q = (10 **(p-1))

while z:
    print(z //q, end =", ")
    z = z % q
    q = q //10
    s = s-1
