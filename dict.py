#Write a Python program that takes a String as an input from the user
# and counts the frequency of each character using a dictionary. 
#For solving this problem, you may use each character as a key and its frequency as values.
#[You are not allowed to use the count() function]
#Hint: You can create a new dictionary to store the frequencies. You may ignore case for simplicity (i.e. may consider P and p to be the same).
#Sample Input: "Python programming is fun"
#Sample Output: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 3, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 's': 1, 'f': 1, 'u': 1}
usr_inp = input("Enter a string: ")
dict1 = {}
for i in usr_inp:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1
print(dict1)

# Write a Python program which will take a list of course codes from the user.
#Create a dictionary from those course codes that will hold the course codes level wise.
# Sample Input: CSE110 CSE111 CSE221 CSE260 CSE320 CSE340 CSE370 CSE421 CSE423
# Sample Output:{"100 Level" : ["CSE110", "CSE111"], "200 Level" : ["CSE221", "CSE260"],
# "300 Level" : ["CSE320", "CSE340" , "CSE370"],  "400 Level" : ["CSE421", "CSE423"]}
lst = input("Enter a list: ").split(", ")
dict = {}
count = 0
for i in range(len(lst)):
    count += 1
    level = lst[i]
    p = str(count) +"_"+level[0:2]+"_"+level[-1:-5]
    if level not in dict:
        nlst = []
        nlst.append(p)
        dict[level] = nlst
        
    else:
        dict[level].append(p)
print(dict)

#Write a Python program that finds the largest value with its key from a given dictionary.
#[You are not allowed to use the max() function for this task]
#Note: You do not need to take the dictionaries as an input from the user but your code should work for any given dictionary.
#Also, you need to handle the quotation marks as a part of the output.
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


#Suppose there is a dictionary named exam_marks as given below.
#exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
#Write a Python program that takes an input from the user and creates a new dictionary 
#with only those elements from 'exam_marks' whose keys have values higher than the user input (inclusive).
#Sample Input 1:170
#Sample Output 1: {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Pierre Cox': 190}
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
p = int(input("enter number: "))
dict = {}
for i in exam_marks:
    if exam_marks[i] >= p:
        dict[i] = exam_marks[i]
print(dict)