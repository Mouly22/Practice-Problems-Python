#Write a Python code for the following: 1) Ask the user to enter the name of his favorite car. 2) Ask the user to enter a Number.
# Display the name of the user’s favorite car, the number of times specified in the second step.
#Sample Input 1: Toyota 2 Sample Output 1: Toyota Toyota
x = "Veyron"
y = 3
for i in range(y):
    print(x)

#Write the Python code of a program that adds all numbers that are multiples of both 7 and 9 up to 600 (including 600) i.e. 63, 126, 189, 252, ....
#The output of your program should be: 2835 (since 63 + 126 + 189 + 252 + 315 + 378 + 441 + 504 + 567 = 2835)
x = 601
p = 0
for i in range(x):
    if i % 7 == 0 and i%9 == 0:
        p = p + i
print(p)


#Write the Python code of a program that adds all numbers that are multiples of either 7 or 9 up to 600 (including 600) i.e. 7, 9, 14, 18, 21, 27, 28, 35, 36..... .Ensure that numbers like 63, 126, 189 which are multiples of both 7 and 9 are added only once in the sum.
#The output of your program should be: 42649
x = 601
r = 0
for i in range(x):
    if i % 7 == 0 or i % 9 == 0:
        r = r + i
print(r)


#Write a Python code of a program that adds all numbers that are multiples of either 7 or 9 but not both, up to 600 (including 600) i.e. 7, 9, 14, 18, 21..... and so on but not the numbers 63, 126, 189..... which are multiples of both 7 and 9.
#The output of your program should be: 39814
x = 601
r = 0
for i in range(x):
    if i % 7 != 0 and i % 9 == 0:
        r = r + i
    elif i % 7 == 0 and i % 9 != 0:
        r = r + i
print(r)

#(*)Write a Python code that will calculate the value of y if the expression of y is as follows (n is the input):
#𝑦=1^2−2^2+3^2−4^2+5^2.........+𝑛^2
#Input 1: 5 Output 1: 15.  Input 2: 10 Output 2: -55. Input 3: 20 Output 3: -210.
x = 20
p =0
for i in range(x+1):
    if i %2 == 0:
        p -= i*i
    else:
        p += i*i
print(p)


#Write a Python code that will read 5 numbers from the user. Your program should print the first number, the sum of the first 2 numbers, the sum of the first 3 numbers, and so on up to the sum of 5 numbers.
#Sample Input 1: 1 2 3 4 5. Sample Output 1: 1 3 6 10 15
g = 0
for i in range(5):
    x = int(input())
    g += x
    print(g)