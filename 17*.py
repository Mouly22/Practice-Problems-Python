#Write a Python program that will ask the user to enter two strings (s1, s2) as an input. Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string.
s1 = "MNOPQRSTUVKKKKKKK"
s2 = "abcdefghjjjjjjj"
p = len(s1)
q = len(s2)
t =""
if p <q :
    r = p
else:
    r = q
for i in range(r):
    t = t+ s1[i]+s2[i]
if p > q:
    t = t + s1[i+1:]
elif q > p:
    t = t + s2[i+1:]
print(t)