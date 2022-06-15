#  From a given string, print the string in all uppercase if the number of uppercase letters is more than lowercase letters. Otherwise, if lowercase is greater or equal to uppercase letters, print all lowercase. The inputs will contain letters (A-Z, a-z) only.
# SampleInput Sample Output
# HOusE        HOUSE
# ApplE        apple
# BaNaNa       banana
p = input("Enter: ")
lst1 = []
lst2 =[]
for i in range(len(p)):
    if 65 <= ord(p[i])<= 90:
        lst1.append(p[i])
    elif 97 <= ord(p[i])<= 122:
        lst2.append(p[i])
if len(lst1) > len(lst2):
    ans = p.upper()
elif len(lst1) <= len(lst2):
    ans = p.lower()
    
print(ans)