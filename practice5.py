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

