# Write a function called rem_duplicate that takes a tuple in the parameter and return a tuple removing all the duplicate values. Then print the returned tuple in the function call.
# [Cannot use remove() or removed() for this task]
# Example1:  Function Call: rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0))
# Output: (1, 2, 3, 4, 5, 6, 0)
# Example2:  Function Call: rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))
# Output: ('Hi', 1, 2, 3, 'a', [1, 2])
def rem_duplicate(x):
    l = list(x)
    b = []
    for i in range(len(l)):
        if l[i] not in b:
            b.append(l[i])
    t = tuple(b)
    print(t)
    
rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))