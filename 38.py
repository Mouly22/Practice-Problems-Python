#Write a Python program that reads 5 numbers into a list and prints the second largest number and its location or index position on the list. [You are not allowed to use the max(), sort(), sorted() function here]
x = []
g = input("Enter 5 numbers: ").split(",")
for i in g:
    x.append(int(i))
temp = None
count = 0
nlst = []
ntemp = None
count1 = 0
for i in range(len(x)):
    if temp == None:
        temp = x[i]
    elif temp < x[i]:
        temp = x[i]
        count = i
for i in range(len(x)):
    if x[i] != temp:
        nlst.append(x[i])

for p in range(len(nlst)):
    if ntemp == None:
        ntemp = nlst[p]
    elif ntemp < nlst[p]:
        ntemp = nlst[p]
        count1 = p

print(ntemp)
print(count1)
print(f"My list: {ff} ")
print(f"Second largest number in the list is {mx1} which was found at index {t}")
