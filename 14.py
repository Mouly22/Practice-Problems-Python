print('''Write a python program that takes the CGPA and no of credits completed by a student and
       prints whether the student is eligible for a waiver and of what percentage. To be eligible for a waiver, 
      a student must have completed at least 30 credits and earned a CGPA greater or equal to 3.8. 
      If not, please print "The student is not eligible for a waiver".
    CGPA     Waiver percentage
3.80 - 3.89       25 percent
3.90 - 3.94       50 percent
3.95 - 3.99       75 percent
4.00             100 percent
Sample Input           Sample Output
3.93
78                     The student is eligible for a waiver of 50 percent
3.79
24                     The student is not eligible for a waiver''')

cg = float(input("Enter your CGPA: "))
credit = int(input("Enter your completed credit: "))

if credit >= 30:
    if cg>= 3.80 and cg<=3.89:
        print("The student is eligible for a waiver of 25 percent")
    elif cg >= 3.90 and cg<= 3.94: 
        print("The student is eligible for a waiver of 50 percent")
    elif cg >= 3.95 and cg<= 3.99:
        print("The student is eligible for a waiver of 75 percent")
    elif cg == 4.00:
        print("The student is eligible for a waiver of 100 percent")
else:
    print("The student is not eligible for a waiver")


