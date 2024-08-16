# Write a python program that splits a given string on a given split character. The first input is a
# String and the second input is the character that will be used to split the first String.
#       Sample                                     Input Output
#       This-is-CSE110                                This
#        -                                             is
#                                                    CSE110

# tom@gmail,harry@yahoo,bob@gmail,mary@gmail,        tom@gmail
#        ,                                           harry@yahoo
#                                                    bob@gmail
#                                                    mary@gmail
     
count = 0
inp = input("Enter input: ")
inp2 = input("Enter Seperation Character: ")
for x in range(len(inp)):
   
    vari = inp.replace(inp2, '\n')
print(vari)



# Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, 
# print “Not a Binary Number”.
# Sample Input                 Output
# 01101101101               Binary Number
# 12344ab0                  Not a Binary Number
# 10127490111              Not a Binary Number
# ary NumberBin            Not a Binary Number

inp = input("Enter Input: ")
for x in range(len(inp)):
    if ord(inp[x]) != 48 and ord(inp[x]) != 49 :
        val ='Not a Binary Number'
        break
    else:
        val ='Binary Number'
print(val)


       
    