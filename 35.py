#Write a Python program that replaces the last element of first list with second list.



l1 = [1, 4, 7, 5]
l2= [6, 1, 3, 9]
l = []
for i in range(len(l1)-1):
    l.append(l1[i])
    c =l + l2
print(c)