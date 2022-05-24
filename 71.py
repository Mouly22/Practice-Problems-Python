# Write a function which will take 4 arguments. They are: 1) starting value(inclusive) 2) ending value(exclusive) 3) first divisor 4) second divisor
# Your first task is to take these arguments as user input and pass these values to the function. Your second task is to implement the function and find all the numbers that are divisible by the first divisor or second divisor but not both from the starting value(inclusive) and ending value(exclusive). Add all the numbers that are divisible and finally return this value. Print the returned value in the function call.
# Input 1:
# 10
# 40
# 4
# 7
# Function Call: function_name(10, 40, 4, 7)
# Output 1: 210
# Input2 :
# 5
# 100
# 3
# 4
# Function Call: function_name(5, 100, 3, 4)
# Output: 2012
def function_name(a, b, c, d):
    rlst =[]
    blst =[]
    count = 0
    for i in range(a, b):
        if i% c == 0 and i % d == 0:
            rlst.append(i)
        elif i % c == 0:
            blst.append(i)
        elif i % d == 0:
            blst.append(i)
    for j in range(len(blst)):
        count += blst[j]
    print(count)
    
function_name(int(input("Enter starting value: ")), int(input("Enter ending value: ")), int(input("Enter first divisor: ")), int(input("Enter second divisor: ")))    

