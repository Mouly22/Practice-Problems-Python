# Given a string, print whether it is a number, word or mixed with digit and letters. If all the characters are numeric values, print NUMBER. If they are all letters, print WORD. If it is mixed, print MIXED.
# Sample Input     Sample Output
# 213213           NUMBER
# jhg231j213       MIXED
# Hello            WORD
x = 'mon45'
if x == str(x):
    p = x.isalpha()              #use isalpha when we want to find if there are any number in a string or not
    if p == False:
        print("MIXED")
    else:
        print("WORD")
elif x == int(x):
    print("NUMBER")