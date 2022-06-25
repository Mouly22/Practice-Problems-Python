#adding two dict together
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}
dict1.update(dict2)
print(dict1)

#if they say dict 1 and 2 will remain unchanged, then we have to copy dict1;then we'll add dict2 with it
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)


#take a input dict from the user
n = 2
d = dict(input("Enter: ").split() for i in range(n))        #while taking input write one key-value in only line and go to the next line
print(d)

#or,
val="""name mouly
age 21
home bogura"""
    
y = dict(x.split() for x in val.splitlines())
print(y)

#or
n = int(input("enter a n value:"))
d = {}
for i in range(n):
    keys = input() # here i have taken keys as strings
    values =input() # here i have taken values as integers
    d[keys] = values
print(d)

#or,
n = int(input())          #n is the number of items you want to enter
d ={}                     
for i in range(n):        
    text = input().split()     #split the input text based on space & store in the list 'text'
    d[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
print(d)

#nested dic
dic  = {}
dic['mouly'] = {}
dic['mouly']['baby1'] = 3
dic['mouly']['baby2'] = 4
print(dic)