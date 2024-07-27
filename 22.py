print('''Write a python program that takes 2 inputs from the user. The first input is a string and the second input is a letter. 
      The program should remove all occurences of the letter from the given string and print the output.
       If the letter is not found in the string and the length of string is greater than 3, 
      then remove the first letter and last letter of the given string and print it. 
      Otherwise print the string as it is. [You can assume that all the input will be in lowercase letter]
Sample Input 1:            Sample output 1:
tanjiro kamado
a                            tnjiro kmdo

Sample Input 2:           Sample Output 2:
eren yeager                 
k                            ren yeage

Sample Input 3:           Sample Output 3:
hi
a                             hi
''')


inp1 = input("Enter a string: ")
inp2 = input("Enter a character: ")
for i in range(len(inp1)):
    if inp2 in inp1:
        var = inp1.replace(inp2, "")
       
    elif inp2 not in inp1:
        if len(inp1) >3:
            var = inp1[1:-1]
        else:
            var = inp1
print(var)

#prev:

var1 = "eren yeager"
var2 = "s"
y = ''
for i in range(len(var1)):
    if var2[0] == var1[i]:
        y = var1.replace(var2[0],'')
    elif var2[0] != var1[i] and len(var1)>3:
        y = var1[1:i]
    else:
        y = var1
print(y)