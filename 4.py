#Write Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds.
#Example01: Input: 10000 Output: Hours: 2 Minutes: 46 Seconds: 40
#==========================================================
#Example02: Input: 500 Output: Hours: 0 Minutes: 8 Seconds: 20
x = 500
hr = x//3600
p = x % 3600
min = p//60
q = p % 60

print("Hours:", hr, "Minutes:", min, "Seconds:", q)


given = int(input())
hrs = given // 3600
p = given % 3600
mns = p // 60
sc = p % 60
print(f'Hours: {hrs} Minutes: {mns} Seconds: {sc}')




#Suppose the following expressions are used to calculate the values of L for different values of S:
#𝐿=3000−125𝑆^2 L= 3000− 125S^2 if  𝑆<100 S<100
#𝐿=120004+𝑆2/14900 L=12000^4+S^2/ 14900 if  𝑆≥100 S ≥ 100
#Write a Python code of a program that reads a value of S and then calculates the value of L.
#Example01: Input: 120 Output: 2416.2162162162163. Example02: Input: 3 Output: 1875
S = 120
if S < 100:
    L = 3000 - (125*(S**2))
    print(L)
elif S >= 100:
    L = 12000/(4 + (S**2 / 14900))
    print(L)











