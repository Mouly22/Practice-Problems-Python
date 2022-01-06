# Write a Python program which will take a list of course codes from the
# user. Create a dictionary from those course codes that will hold the course codes level wise.
# Sample Input: CSE110 CSE111 CSE221 CSE260 CSE320 CSE340 CSE370 CSE421 CSE423
# Sample Output:{"100 Level" : ["CSE110", "CSE111"], "200 Level" : ["CSE221", "CSE260"],
# "300 Level" : ["CSE320", "CSE340" , "CSE370"],  "400 Level" : ["CSE421", "CSE423"]}
lst = input("Enter course code: ").split()
dict = {}
for i in range(len(lst)):
    x = lst[i]
    n = str(int(x[3])* 100) + " Level"
    #print(n)
    if n not in dict:
        lst1 = []
        lst1.append(x)
        dict[n] = lst1
    else:
        dict[n].append(x)
print(dict)
