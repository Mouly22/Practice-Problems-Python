#Write a Python program that finds the largest value with its key from a given dictionary.
#[You are not allowed to use the max() function for this task]
#Note: You do not need to take the dictionaries as an input from the user but your code should work for any given dictionary. Also, you need to handle the quotation marks as a part of the output.
#Hint: Think of membership operators (in and not in). You can use dictionary functions to get the values.
#Sample 1: {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
#Output: The highest selling book genre is 'mystery' and the number of books sold are 15.

dict1 = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
maxval = 0
maxs = ''
for x,y in dict1.items():
    if y > maxval:
        maxval = y
        maxs = x
print(f"The highest selling book genre is", maxs, f"and the number of books sold are ", maxval)
