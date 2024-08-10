print('''Write a Python program that asks the user for a quantity, then takes that many numbers as input and 
prints the maximum, minimum and average of those numbers.
Example: If the user enters 5 as an input for quantity and the enters the 5 numbers, 10, 4, -1, -100, and 1.
The output of your program should be: “Maximum 10”, “Minimum -100”, “Average is -17.2”''')

inp1 = int(input("Enter the quantity: "))
suming = 0
for x in range(inp1):
    inp2 = int(input("Enter number: "))
    if x == 0:
        u = inp2
        v = inp2
    if x > 0:
        if u> inp2:
            u = u
        else:
            u = inp2
        if v > inp2:
            v = inp2
        else:
            v = v
    suming += inp2
    avg = suming/inp1
    

print('Max Number: '+ str(u))
print('Min Number: '+ str(v))
print('Average Number: '+ str(avg))


#prev
x = int(input("Enter the amount ")) 
summ = 0
t = 0
mx = None
mn = None
for i in range(x):
    xx = int(input("Here "))
    if mx == None:
        mx = xx
    elif xx > mx:
        mx = xx
    if mn == None:
        mn = xx
    elif xx < mn:
        mn = xx
    summ += xx
print(f"Maximum {mx}")
print(f"Mininum {mn}")
avg = summ/x
print(f"Average {avg}")
