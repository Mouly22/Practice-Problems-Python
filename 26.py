# Write a Python program that will ask the user to input a string (containing exactly one
# word). Then print the ASCII code for each character in the String using the ord( ) function.
#       Sample Input                 Sample Output
#       quincuncial                     q: 113
#                                       u: 117
#                                       i: 105
#                                       n: 110
#                                       c: 99
#                                       u: 117
#                                       n: 110
#                                       c: 99
#                                       i: 105
#                                       a: 97
#                                       l: 108

inp = input("Enter Input: ")
for x in inp:
    print(x+': '+str(ord(x)))

# Write a Python program that takes a String as input from the user, removes the characters
# at even index and prints the resulting String in uppercase.
# Sample Input                  Output
#    String                      TIG
#    abcd                        BD


inps = input("Enter Input: ")
for x in range(len(inps)):
    if x % 2 != 0:
        val = ord(inps[x])
        if val >= 97 or val <= 122:
            val -= 32
            val2 = chr(val)
        print(val2, end = '')
