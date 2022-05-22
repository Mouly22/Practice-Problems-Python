# Write a function which will take 1 argument, number of days.Your first task is to take the number of days as user input and pass the value to the function. Your second task is to implement the function and calculate the total number of years, number of months, and the remaining number of days as output. No need to return any value, print inside the function.
# Note: Assume, each year to be 365 days and month to be 30 days.
# Example01
# Input: 4330
# Function Call: function_name(4330)
# Output: 11 years, 10 months and 15 days
# Example02
# Input: 2250
# Function Call: function_name(2250)
# Output: 6 years, 2 months and 0 days
def function_name(x):
    y = x // 365
    vag = x % 365 
    p = vag // 30
    d = vag % 30
    print(f"{y} years, {p} months, {d} days")
function_name(int(input("Enter number of days: ")))