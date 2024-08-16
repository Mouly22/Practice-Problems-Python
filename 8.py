# Write a Python program that takes a number as input from the user and prints the divisors of that number
#        as well as how many divisors the number has.
#       Sample Input 1:          Sample Output 1:
#            6                          1
#                                       2
#                                       3
#                                       6
#                               Total 4 divisors.

count = 0
number = int(input("Enter a number: "))
for i in range(1, number+1):
    if number % i == 0:
        val = i
        count +=1
        print(i)
print("Total " + str(count) + " divisor(s).")








#before
x = input()
xx = int(x)
count = 0
for i in range(1, xx+1):
    d = xx % i
    if d == 0:
        count += 1
        print(i)
print(f"Total {count} divisors.")

