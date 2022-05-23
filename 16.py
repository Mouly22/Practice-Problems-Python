#Write a Python program that will ask the user to input a string (containing exactly one word). Then print the ASCII code for each character in the String using the ord() function.
x = input()
for i in range(len(x)):
    print(f"{x[i]} : {ord(x[i])}")

#Take a string as a input from the user with all small letters. Then print the next alphabet in sequence for each alphabet found in the input.
x = input()
g = ""
for i in range(len(x)):
    y = ord(x[i])+1
    if y == 123:
        print(chr(97), end='')
    else:
        print(chr(y), end ='')
        