# Assume, you have been given a tuple as below.
# a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]). Write a Python program that asks the user for an input (can be any data type) and replaces the last element of each of the inner lists with the user given value.
# Sample Input 1: abc Sample Output 1: ([1, 2, 'abc'], [4, 5, 'abc'], [7, 8, 'abc'], [10, 11, 'abc'])
# Sample Input 2: 1000  Sample Output 2:  ([1, 2, '1000'], [4, 5, '1000'], [7, 8, '1000'], [10, 11, '1000'])
ple = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]) 

z = []
k = 1000
a,b,c,d = ple
g = [a,b,c,d]
for i in g:
    if i[-1] != k:
        i[-1] = k

print(tuple(g))