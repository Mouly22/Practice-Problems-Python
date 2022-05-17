# Write a Python program that finds the largest value with its key from a given dictionary. [You are not allowed to use the max() function for this task]
# Given:
# {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
# Output:
# The highest selling book genre is 'mystery' and the number of books sold are 15.
g = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14 }
c = {}
s = None
for u,v in g.items():
    if s == None:
        s = v
        c = u
    elif s <= v:
        s = v
        c = u
print(f"The highest selling book genre is {c} and the number of books sold are {s}")