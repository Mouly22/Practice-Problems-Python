#Write a Python program that takes a dictionary as an input from the user 
#and then prints the average of all the values in the dictionary.
#[You are not allowed to use len() and sum()]
#Sample Input 1:
#{'Jon': 100, 'Dan':200, 'Rob':300}
#Sample Output 1:
#Average is 200.
lst = input("Enter: ")
p = lst[1: -1].split(', ')
#print(p)
dict = {}
for i in p:
    nval = i.split(':')
    dict.update({nval[0][1: -1]:int(nval[1])})
print(dict)
val = 0
count = 0
for i in dict.values():
    val += i
    count += 1
average = val / count
print(average)













