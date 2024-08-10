#Write a Python program that takes a String as an input from the user and prints that String
# in reverse order.
#  Input    Output
# CSE110    011ESC
# Python    nohtyP
# 1576527   7256751

inp = input("Enter Input value: ")
for x in inp:
    val = inp[::-1]
print(val)

# Write a python program that takes 2 inputs from the user, where the first input is a string with length 
# greater than 1. The second input is the index of the first given string from where you have to start reversing. 
# After reversing the first input string from that index, print the new string back to the user. See samples below 
# for clarification.
#     Sample Input             Sample Output
#      72418                      81427
#       4

#      12345                      32145
#       2

#     aBcd1234defg                21dcBa34defg
#      5

inp1 = input("Enter Input: ")
inp2 = int(input("Enter Index No: "))
for x in inp1:
    val = inp1[0:inp2+1]
    val2 = val[::-1]+ inp1[inp2+1::]
print(val2)
   

