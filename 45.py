#Write a Python program to reverse a given tuple.[You are not allowed to use tuple slicing]
#Example 1: Given tuple: ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')     Output: ('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
g = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') 
f = []
s =[]
r = ()
for i in g:
    f.append(i)
for i in range(len(f)):
    s = f[-1::-1]
for i in range(len(s)):
    r = tuple(s)
print(r)