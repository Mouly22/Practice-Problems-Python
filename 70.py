# Write a function called remove_odd that takes a list of numbers that have both even and odd numbers mixed. 
# Your function should remove all the odd numbers and return a compact list which only contains the even numbers. [Cannot use remove() or removed() for this task]
# Example1: 
# Function Call: remove_odd ([21, 33, 44, 66, 11, 1, 88, 45, 10, 9])
# Output: [44, 66, 88, 10]
# Example2: 
# Function Call: remove_odd ([11,2,3,4,5,2,0,5,3])
# Output: [2, 4, 2, 0]
def remove_odd(lst):
    blst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            blst.append(lst[i])
    print(blst)

remove_odd([11,2,3,4,5,2,0,5,3])