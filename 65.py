# Write a function called make_square that takes a tuple in the parameter as a range of numbers (starting point and ending point (included)). The function should return a dictionary with the numbers as keys and its squares as values.
# Example1:  Function Call: make_square((1,3))     Output: {1: 1, 2: 4, 3: 9}
# Example2:  Function Call: make_square((5,9))     Output: {5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
def make_square(x):
    a,b = x
    sc ={}
    for i in range(a, b+1):
        if i not in sc:
            sc[i] = i*i
        else:
            sc[i] += i*i
    print(sc)
make_square((5, 9))