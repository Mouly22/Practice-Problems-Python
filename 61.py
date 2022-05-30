# Write a function called calculate_tax that takes 3 arguments: your age, salary, and current job designation.
# Your first task is to take these arguments as user input and pass these values to the function.
# Your second task is to implement the function and calculate the tax as the following conditions:
# NO TAX IF YOU ARE LESS THAN 18 YEARS OLD.
# NO TAX IF YOU ARE THE PRESIDENT OF THE COMPANY
# No tax if you get paid less than 10,000
# 5% tax if you get paid between 10K and 20K
# 10% tax if you get paid more than 20K
# Finally return this tax value. Then print the returned value in the function call.
# Example1: 
# Input:
# 16
# 20000
# Student
# Function Call: calculate_tax(16, 20000, 'Student')
# Output: 0
# Example2: 
# Input:
# 20
# 18000
# assistant manager
# Function Call: calculate_tax(20, 18000, 'assistant manager')
# Output: 900.0
# Example3: 
# Input:
# 20
# 22000
# assistant manager
# Function Call: calculate_tax(20, 22000, 'Assistant manager')
# Output: 2200.0
# Example4: 
# Input:
# 20
# 122000
# president
# Function Call: calculate_tax(20, 122000, 'president')
# Output: 0
def calculate_tax(age, slry, job):
    if age <= 18:
        return 0
    elif job == "president":
        return 0
    elif slry < 10000:
        return 0
    elif slry>= 10000 and slry <= 20000:
        c = (5/ 100)* slry
        return c
    elif slry > 20000:
        d = (10/ 100) * slry
        return d
print(calculate_tax(20, 22000, 'student'))