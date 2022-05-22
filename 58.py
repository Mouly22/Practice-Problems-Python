# Write a python function that takes the limit as an argument of the Fibonacci series and prints till that limit.
# Function Call:
# fibonacci(10)     Output: 0 1 1 2 3 5 8
# fibonacci(5)      Output: 0 1 1 2 3 5
def fibonacci(x):
    n1 = 0
    n2 = 1
    total = 0
    while total < x:
        print(total)
        n1 = n2
        n2 = total
        total = n1 + n2
fibonacci(15)