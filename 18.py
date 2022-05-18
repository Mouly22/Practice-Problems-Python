#Given a string, create a new string with all the consecutive duplicates removed.
x = "AAABBBBCDDBBECE"
p = ""
for i in range(len(x)):
    if x[i] != x[i-1]:
        p = x[i]
        print(p, end='')