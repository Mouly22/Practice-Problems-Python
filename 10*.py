print('''Write a Python program that asks the user for a quantity, 
then takes that many numbers as input and prints the maximum, minimum and average of those numbers.''')
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
