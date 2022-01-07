#Write a Python program that takes a String as an input from the user
# and counts the frequency of each character using a dictionary. 
#For solving this problem, you may use each character as a key and its frequency as values.
#[You are not allowed to use the count() function]
#Hint: You can create a new dictionary to store the frequencies. You may ignore case for simplicity (i.e. may consider P and p to be the same).
#Sample Input: "Python programming is fun"
#Sample Output: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 3, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 's': 1, 'f': 1, 'u': 1}
taken = input("Enter a string: ")
taken = taken.lower()
taken = taken.replace(" ", '')
dict = {}
for i in taken:
    if taken not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
    
print(dict)