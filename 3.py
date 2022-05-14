#Write Python code of a program that reads an integer, and prints the integer if it is a multiple of either 2 or 5.
#Input:5 Output: 5.  Input: 3 Output: Not a multiple
x = 3
if x% 2 == 0 or x% 5 == 0:
    print(x)
else:
    print("Not a multiple")

#Write Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both.
#Input: 10 Output: multiple of 2 and 5 both  Input: 5 Output: 5
x = 5
if x% 2 ==0 and x% 5 ==0:
    print("both")
else:
    print(x)

#Write Python code of a program that reads an integer, and prints the integer if it is a multiple of 2 and 5.
#Input:5 Output: Not multiple of 2 and 5 both. Input:40 Output: 40
x = 5
if x% 2 == 0 and x% 5 ==0:
    print(x)
else:
    print("Not multiple of 2 and 5 both")

#Write Python code of a program that reads an integer, and prints the integer if it is a multiple of NEITHER 2 NOR 5.
#Input:3 Output:3. Input: 5 Output: No
x = 12
if x % 2 != 0 and x%5 != 0:
    print(x)
else:
    print("No")