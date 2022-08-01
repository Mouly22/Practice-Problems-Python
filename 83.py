# my_tuple = ("UK NoTimeToDie DanielCraige", "USA MissionImpossible TomCruise", "USA TopGun TomCruise", "USA Troy BradPitt",
# "UK Skyfall DanielCraige", "UK TheTheoryOfEveryting EddieRedmayne", "UK FantasticBeast EddieRedmayne", "USA Seven BradPitt")

# Your task is to write a python program that will create an ID for all the movies and store it in a dictionary and then print the dictionary.
# Your dictionary should be as expected output and while generating the ID ensure the following criteria are met. Finally print the dictionary.

# For the first digit, if country is UK = 2 and USA = 1
# Then, if actor is DanielCraige = 04, TomCruise = 03, BradPitt = 02 and EddieRedmayne = 01
# Use the tuple’s index number as the last digit.

# Expected Output:
# {'USA': [('MissionImpossible', 1031), ('TopGun', 1032), ('Troy', 1023), ('Seven', 1027)], 
# 'UK': [('NoTimeToDie', 2040), ('Skyfall', 2044), ('TheTheoryOfEveryting', 2015), ('FantasticBeast', 2016)]}

# Explanation: ID of MissionImpossible is 1031. This actor is from the USA so the first digit is 1,
# as the actor is TomCruise so 2nd and 3rd digits are 03 and last digit 1 represents that item is situated at index 1 in the my_tuple.
# You must store the movie name and movie ID in a tuple and save that tuple in a list as the value of the dictionary. 
# You Must Store The ID as an Integer.

my_tuple = ("UK NoTimeToDie DanielCraige", "USA MissionImpossible TomCruise", "USA TopGun TomCruise", "USA Troy BradPitt", "UK Skyfall DanielCraige", "UK TheTheoryOfEveryting EddieRedmayne", "UK FantasticBeast EddieRedmayne", "USA Seven BradPitt")
lst1 = []
lst2 = []
lst3 = []
dct = {}
temp = ''
for elm in my_tuple:
    lst1.append(elm)


for x in range(len(lst1)):
    a = lst1[x].split(' ')
    lst2.append(a)

for z in range(len(lst2)):
    if lst2[z][0] == 'USA':
        temp = '1'
    elif lst2[z][0] == "UK":
        temp = '2'
    if lst2[z][2] == 'EddieRedmayne':
        temp += '01'
    elif lst2[z][2] == 'BradPitt':
        temp +='02'
    elif lst2[z][2] == 'TomCruise':
        temp +='03'
    elif lst2[z][2] == 'DanielCraige':
        temp += '04'
    if lst2[z][1] == 'NoTimeToDie':
        temp += '0'
    elif lst2[z][1] == 'MissionImpossible':
        temp += '1'
    elif lst2[z][1] == 'TopGun':
        temp += '2'
    elif lst2[z][1] == 'Troy':
        temp += '3'
    elif lst2[z][1] == 'Skyfall':
        temp += '4'
    elif lst2[z][1] == 'TheTheoryOfEveryting':
        temp += '5'
    elif lst2[z][1] == 'FantasticBeast':
        temp += '6'
    elif lst2[z][1] == 'Seven':
        temp += '7'
    temp = int(temp)

    if lst2[z][0] not in dct.keys():
        dct[lst2[z][0]] = [(lst2[z][1], temp)]
    else:
        dct[lst2[z][0]].append((lst2[z][1], temp))

print(dct)