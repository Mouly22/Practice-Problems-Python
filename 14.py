#Write a Python program that will ask the user to input a string (containing exactly one word). Then your program should print subsequent substrings of the given string as shown in the examples below.
x = "DREAM"
for i in range(len(x)+1):
    print(x[:i])

x = "DREAM"
for i in range(len(x)+1):
    print(x[i:])