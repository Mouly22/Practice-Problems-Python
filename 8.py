#Write a Python program that takes a number as input from the user and prints the divisors of that number as well as how many divisors the number has.
x = input()
xx = int(x)
count = 0
for i in range(1, xx+1):
    d = xx % i
    if d == 0:
        count += 1
        print(i)
print(f"Total {count} divisors.")

