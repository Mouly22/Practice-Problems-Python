#n = input("ENTER watch: ").split()
dict = {}
while(True):
    n = input("ENTER watch: ").split()
    if n == "STOP":
        break
    else:
        if n not in dict:
            dict.update({n : 1})
        else:
            dict[n] += 1

print(dict)