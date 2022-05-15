#Write a Python program that reads 5 numbers into a list and prints the second largest number and its location or index position on the list. [You are not allowed to use the max(), sort(), sorted() function here]
g = input("Enter 5 numbers: ").split(",")
ff=[]
mx = None
mm =[]
mx1 = None
t = 0
for i in g:
    ff.append(int(i))
for i in range(len(ff)):
    if mx == None:
        mx = ff[i]
    elif mx < ff[i]:
        mx = ff[i]
for i in range(len(ff)):
    if mx != ff[i]:
        mm.append(ff[i])
for i in range(len(mm)):
    if mx1 == None:
        mx1 = mm[i]
    elif mx1 < mm[i]:
        mx1 = mm[i]
        t = i
print(f"My list: {ff} ")
print(f"Second largest number in the list is {mx1} which was found at index {t}")