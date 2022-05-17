#Assume, you have been given a tuple. Write a Python program that creates a new tuple excluding the first and last two elements of the given tuple and prints the new tuple.
# Sample Input 1:
# (10, 20, 24, 25, 26, 35, 70)
# Sample Output 1:
# (24, 25, 26)
y = (-10, 20, 25, 30, 40)
for i in range(len(y)):
    c = y[2:-2]
print(c)