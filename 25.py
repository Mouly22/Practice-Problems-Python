print('''Write a Python program that takes a number from the user and prints its digits from left to right.
[Consider the input number to be an INTEGER. You are not allowed to use String indexing for
solving this task]
Example: if the user gives 32768, then print 3, 2, 7, 6, 8
===============================================================
Hint(1): The input() function takes the input data as String data type by default. Please convert it
to an integer before starting your code for the task.
Hint(2):
Step 1: First, count how many digits are there in the input number
Step 2: Then, calculate 10 to the power (number of digits - 1).
Step 3 with explanation: Say, the input given by the user as in our example, 32768 has 5 digits,
so calculating 10 to the power 4 gives us 10000. Then floor dividing 32768 by 10000, we can get 3.
      
Proceeding further, the remainder of 32768 by 10000 (32768 % 10000) gives us 2768. This time
to get 2 we need to floor divide 2768 by 1000 which is basically our 10000/10. Again, taking the
remainder of 2768 by 1000 gives us 768 which we then divide by 100 (i.e. 1000/10) and keep on
doing this until there are no more digits left (zero).
      ''')

count = 0
inp = input("Enter NUmber: ")
for i in range(len(inp)):
    count += 1
inp2 = int(inp)
for x in range(count):
    val = 10**(count-1-x)
    divi = inp2//val
    remi = inp2 % val
    inp2 = remi
    
    print(divi, end = ' ')
    #print(remi)








    
