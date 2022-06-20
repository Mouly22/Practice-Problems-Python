# Write a python program that will take N as input from the user and then take N lines of input from the user. Each line will contain a tennis player name, year and tournament name that he won that year. Store each player's championship information in a dictionary where the key will be the player name and corresponding value will be a list containing all the tournaments the player won along with the year of the tournament. 
# Sample Input 1:
# 6
# 2021 AustralianOpen Djokovic
# 2021 FrenchOpen Djokovic
# 2020 FrenchOpen Nadal
# 2020 USOpen Dominic
# 2020 AustralianOpen Djokovic
# 2019 USOpen Nadal
# Sample Output 1 (No need to follow this output format. Just print the resultant dictionary. ):
# {'Djokovic': {2021:['AustralianOpen','FrenchOpen'], 2020:['AustralianOpen']}, 'Nadal': {2020:['FrenchOpen'], 2019: ['USOpen']}, 'Dominic': {2020:['USOpen']}}
n = int(input("Enter number: "))
lst=[]
dic1 = {}
for i in range(n):
    inp = input().split(' ')
    lst.append(inp)
for p in lst:
    if p[-1] not in dic1.keys():
        dic1[p[-1]] = {p[0]:[p[1]]}
    else:
        if p[0] not in dic1[p[-1]].keys():
            dic1[p[-1]][p[0]] = [p[1]]
        else:
            dic1[p[-1]][p[0]].append(p[1])
print(dic1)