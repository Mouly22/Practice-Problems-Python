# Given a string, print whether it is a number, word or mixed with digit and letters. If all the characters are numeric values, print NUMBER. If they are all letters, print WORD. If it is mixed, print MIXED.
# Sample Input     Sample Output
# 213213           NUMBER
# jhg231j213       MIXED
# Hello            WORD
p = 23445

if p == str(p):
    q = p.isalpha()
    if q == False:
        print("MIXED")
    else:
        print("WORD")
else:
    if p == int(p):
        print("NUMBER")