# Write a Python program that takes a dictionary as an input from the user and then prints the average of all the values in the dictionary.[You are not allowed to use len() and sum()]
# Sample Input 1: {'Jon': 100, 'Dan':200, 'Rob':300}.   Sample Output 1:  Average is 200.
c = {'Jon': 100, 'Dan':200, 'Rob':300}
summ = 0
count = 0
for i in c.values():
    summ += i
    count+= 1
avg = summ//count
print(avg) 