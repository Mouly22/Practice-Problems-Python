#Write a Python program that takes two lists as an input from the user. Then print a new list with the common elements of both the input lists.
p = [1, 3, 'A', 'H', 'P']
q = ['A', 'G', 1, 'P', 'O']
gg = []
for i in range(len(p)):
    if p[i] in q:
        gg.append(p[i])
print(gg)