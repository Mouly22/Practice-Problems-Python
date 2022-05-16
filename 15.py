#Write a Python program that will ask the user to enter a word as an input.
#If the length of the input string is less than 4, then your program should print the same string as an output.
#If the input string’s length is greater than 3, then your program should add "er" at the end of the input string.
#If the input string already ends with "er", then add "est" instead.
#If the input string already ends with "est", then your program should print the same input string as an output
x = input("Enter a word: ")
y = len(x)
z = ""

if y >3: 
    if x.endswith('est'):
        z = x
    elif x.endswith('er'):
        z = x.replace('er','est')
    else:
        z = x + 'er'
else:
    if y < 4:
        z = x
print(z)