#Given a string, create a new string with all the consecutive duplicates removed.
x = "AAABBBBCDDBBECE"
p = ""
for i in range(len(x)):
    if x[i] != x[i-1]:
        p = x[i]
        print(p, end='')

#Write a python program that takes 2 inputs from the user, where the first input is a string with length greater than 1.
#The second input is the index of the first given string from where you have to start reversing. 
#Then print the new string back to the user.
n = "aBcd1234defg"
p = 5
for i in range(len(n)):
    if p == i:
        print((n[i::-1]) +n[i+1:])