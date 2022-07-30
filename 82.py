# Write a Python program that takes multiple words as input from the user and calculates the frequency of each word. Finally, print all the words (sorted in ascending order) grouped by frequency (sorted in descending order).[You can not use built in .count() function]
# Sample Input #1: cow cat cow ant elephant cow dog lion cat goat cow lion tiger elephant
# Sample Output #2:
#  {
#  4 : ['cow'],
#  2 : ['cat', 'elephant', 'lion'],
#  1 : ['ant', 'dog', 'goat', 'tiger']
#  }
#  Sample Input #2:
#  cat dog lion cat elephant goat cow lion ant tiger elephant cow cow cow
#  Sample Output #2:
#  {
#  4 : ['cow'],
#  2 : ['cat', 'elephant', 'lion'],
#  1 : ['ant', 'dog', 'goat', 'tiger']
#  }
#Approach no 1:
y = 'cow', 'cat', 'cow', 'ant', 'elephant', 'cow', 'dog', 'lion', 'cat', 'goat', 'cow', 'lion', 'tiger', 'elephant'
lst = []
dct = {}
for i in range(len(y)):
    lst.append(y[i])
    
for j in lst:
    val = lst.count(j)
    if val not in dct.keys():
        dct[val] = [j]
    else:
        if j in dct[val]:
            pass
        else:
            dct[val].append(j)

print(dct)  
#Approach no 2:
y = 'cow', 'cat', 'cow', 'ant', 'elephant', 'cow', 'dog', 'lion', 'cat', 'goat', 'cow', 'lion', 'tiger', 'elephant'
lst = []
dct = {}
dct2 = {}
for i in range(len(y)):
    lst.append(y[i])
for j in lst:
    val = lst.count(j)
    if j not in dct.keys():
        dct[j] = [val]
for m, n in dct.items():
    for x in n:
        if x not in dct2.keys():
            dct2[x] = [m]
        else:
            dct2[x].append(m)
print(dct2)