# Write a function called even_checker that takes a number as an argument and prints whether the number is even or odd inside the function.
# Example1:                              Example2: 
# Function Call:                         Function Call:
# even_checker(5)                        even_checker(2)
# Output: Odd!!                          Output: Even!!
def even_checker(v):
    if v%2 == 0:
        print("Even!!")
    else:
        print("Odd!!")
even_checker(int(input("Enter: ")))