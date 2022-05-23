# You have been hired as an app developer for the company. The company plans to make an app for a grocery store where the user can order groceries and see the total amount to be paid in the cart section. To build this feature, you have to write a function that takes 2 arguments. They are:
# 1)order_items (must be a list) 2)location (default value should be set to "Dhanmondi")
# Your first task is to take a list of items from the user. Pass the list into the function parameter along with the optional location (Use default argument technique). (Also, no need to take location as input, pass this any value you want.)
# Your second task is to implement the function. In the function, create a dictionary for the items shown in the table. Calculate the total price of the items passed as a list to the function. Additionally, add a delivery fee of 30 taka if the location is Dhanmondi. Otherwise, add a delivery fee of 70 taka. Finally, return the value and print it.
# Item	Price(Tk)
# Rice	    105
# Potato	20
# Chicken	250
# Beef	    510
# Oil	    85
# Example1:
# function_name(["Rice", "Beef", "Rice"], "Mohakhali")
# total = 105 + 510 + 105 = 720 (Take the price of each item and add them.)
# total = 720 + 70 = 790 (Finally, add the delivery fee based on the location.)
# Input: ["Rice", "Beef", "Rice"]
# Function Call: function_name(["Rice", "Beef", "Rice"], "Mohakhali")
# Output: 790

# Example2:
# function_name(["Rice", "Beef", "Rice"])
# total = 105 + 510 + 105 = 720 (Take the price of each item and add them.)
# total = 720 + 30 = 750 (Since no location is passed in the parameter, it will use the default location-"Dhanmondi". For dhanmondi, delivery fee of 30 taka)
# Input: ["Rice", "Beef", "Rice"]
# Function Call: function_name(["Rice", "Beef", "Rice"])
# Output: 750
def function_name(x, y = "Dhanmondi"):
    dct = {'Rice': 105, 'Potato': 20, 'Chicken': 250, 'Beef': 510, 'Oil': 85}
    li = []
    total = 0
    for p in x:
        li.append(p)
    for q in li:
        total += dct[q]
    if y != "Dhanmondi":
        total += 70
    else:
        total += 30
    print(total)

function_name(input("Enter your items: ").split(", "), input("Enter your location: "))
