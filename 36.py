#Write a Python program that turns every item of a list into its square.
y = [1, 2, 3, 4, 5, 6, 7]
g =[]
for i in range(len(y)):
    c = y[i]*y[i]
    g.append(c)
print(g)