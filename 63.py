# Write a function called show_palindrome that takes a number as an argument and then returns a palindrome string. Finally, prints the returned value in the function call.
# Example1: 
# Function Call: show_palindrome(5)
# Output: 123454321
# Example2: 
# Function Call: show_palindrome(3)
# Output: 12321
def show_palindrome(x):
    b = []
    for i in range(x):
        a = i + 1
        b.append(a)
        c = b + b[-2::-1]
    for j in c:
        d = ''.join(str(j))
        print(d, end ='')
show_palindrome(5)