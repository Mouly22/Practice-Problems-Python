# Write a Python program to find the first appearance of the substring 'too' and 'good' from a given string. If 'good' follows the 'too', replace the whole 'too'' good' substring with 'excellent' and print the resulting string. If the above does not appear, print the string as it is.
# Sample Input                             Sample Output
# The book is not too good!                The book is not excellent!
# This book is good too!                   This book is good too!
z ='This book is too good too read !'
k = 'too'
m = 'good'
p = ''
count = 0
p = z.split()
lst = []
for i in p:
    lst.append(i)

for i in range(len(lst)):
    if lst[i] == k:
        count += 1
        if count <= 1 and lst[i+1] == m:
            lst[i] = ''
            lst[i+1] = 'excellent'
        else:
            lst = lst

for we in lst:
    if we == '':
        lst.remove(we)
for l in lst:
    s = ''.join(str(l))
    print(s, end = ' ')

