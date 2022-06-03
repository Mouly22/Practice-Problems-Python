# Create a string from two given strings by concatenating common characters of the given strings.
# Sample Input             Sample Output
# harry, hermione          hrrhr
# dean, tom                Nothing in common.
a1 = 'harry'
a2 = 'hermione'
b1 = len(a1)
b2 = len(a2)
count = 0
factor = 0
lst1 = []
if b1 > b2:
    p = b2
elif b1 < b2:
    p = b1
for v in range(p):
    if a1[v] not in a2[v]:
        g = "Nothing in common"
    else:
        for i in range(p):
            if a1[i] in a2[i]:
                count += 1
                if count >= 1:
                    lst1.append(a1[i])
                if count > 1:
                    lst1.append(a1[i])
        for j in range(p):
            if a2[j] in a1[j]:
                factor += 1
                if factor >= 1:
                    lst1.append(a2[j])
        
        for i in lst1:
            g = ''.join(lst1)
print(g)