#Write a Python program that takes a number as input from the user and tells if it is a perfect number or not.
#Sample Input 1:6. Sample Output 1: 6 is a perfect number
x = input()
xx = int(x)
count = 0
sum = 0
for i in range(1, xx+1):
    if xx% i == 0 and i < xx:
        sum += i
        if sum == xx:
            z = f"{xx} is a perfect number"
        else:
            z = f"{xx} is not a perfect number"
print(z)

#Write a Python program that asks the user for one number and tells if it is a prime number or not.
x = input()
xx = int(x)
count = 0
for i in range(1, xx+1):
    if xx % i == 0:
        count += 1
        if count > 2:
            z = f"{xx} is not a prime number"
        else:
            z = f"{xx} is a prime number"
print(z)

