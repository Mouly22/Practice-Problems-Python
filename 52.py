# Given a list of tuples, your task is to multiply the elements of the tuple and return a list of multiplied elements as shown below.
# Example 1:[(2, 3), (4, 5), (6, 7), (2, 8)]
# Output:[6, 20, 42, 16]
p = [(11, 22), (33, 55), (55, 77), (11, 44)]
ls = []
for i in p:
    c = i[0]*i[1]
    ls.append(c)
print(ls)