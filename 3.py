#The Maximum weight

print('''A sailor has a boat known as Téssares Boat, which has four corners. The boat is capable of
carrying goods of any weight as long as there is equal distribution of loads on each corner of the
boat - the center area has been occupied by the engine. The sailor needs your help to know the
maximum amount of weight he can carry in each shipment.
Write a Python program that reads the total weight of the shipment and prints the maximum load
(or weight) the boat can take from the given shipment. We can assume that the weight of each
good is exactly 1 unit, therefore, the weight of 5 units means there are 5 (loose) items in the
shipment. ''')

weight = int(input("Enter total weight: "))
#As there as only four corners, we can assume of keeping amounts of goods that are equal to the multiplier of four
if weight % 4 == 0:
    val = weight
elif weight % 4 != 0:
    val = weight - (weight % 4)
print(val)


print('''Write a python program that takes an integer from the user which represents the number of
chocolates that he/she has. He/She decided to distribute the chocolates equally among 3 friends,
keeping the remaining chocolates for him/herself. Find out the number of chocolates each friend
will receive and the number of chocolates that will be remaining.''')

print('''Sample Input: 50
      Sample Output: Each friend will receive 16 chocolates
                     The number of remaining chocolates is 2
      ''')

choco = int(input("Enter chocolate amount: "))
if choco % 3 == 0:
    val = choco / 3
    rem = 0
 

elif choco % 3 != 0:
    val = choco //3
    rem = choco % 3
print(int(val))
print(int(rem))
