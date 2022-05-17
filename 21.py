#Write a python program that takes two inputs. The first input is a string and the second input is a number. If the number is even then concatenate the given string two times the given number and if the number is odd then concatenate the given string three times the given number.
x = "CSE110"
p = int(input())

if p % 2 == 0:
    y = p*2
else:
    y = p*3
for i in range(y):
    print(x,end='')