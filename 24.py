#finding prime number

number = int(input("Enter a number: "))
count = 0
for i in range(1, number+1):
    if number == 1:
        var = "Not a prime number"
   

    elif number % i == 0:
        count += 1
        if count > 2:
            var ="Not a Prime Number."
        else:
            var="Prime Number."
print(var)
