# Write a python program that takes an input from the user and finds the number of times that the input is present in a given tuple.
# Example 1: Given tuple: (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2) 
# Sample Input 1: 8.  Sample Output 1: 8 appears 4 times in the tuple
g = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2) 
p = 1
count = 0
for i in range(len(g)):
    if g[i] == p:
        count =  count + 1
print(f"{p} appears {count} times in the tuple")