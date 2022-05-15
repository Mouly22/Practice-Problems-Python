#Write a Python program that reads 5 numbers into a list and prints the smallest and largest number and their locations in the list. [You are not allowed to use the max(), min(), sort(), sorted() functions here]
x = input("Enter 5 numbers: ").split(',')
g = []
mx = None
xc = 0
mn = None
xm = 0
for i in x:
    g.append(int(i))
for i in range(len(g)):
    if mx == None:
        mx = g[i]
    elif mx < g[i]:
        mx = g[i]
        xc = i
for i in range(len(g)):        
    if mn == None:
        mn = g[i]
    elif mn > g[i]:
        mn = g[i]
        xm = i
print(f"My list: {g}")
print(f"Smallest number in the list is {mn} which was found at index {xm}")
print(f"Largest number in the list is {mx} which was found at index {xc}")