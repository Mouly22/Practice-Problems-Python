vamp = input("Enter vamp name: ")
print("Edward: Hi, Let me introduce myself! I am" +" " + vamp+ " "+ "and you are Bella right?")
print("Bella: Yeah, You were absent for the past few days? ")
lawn = "Katty Mplier Zone of the Alaska"
print("Edward: Yeah, I was out of town to measure the length of"+ " " + lawn+ " " + "lawn.")
print("Bella: is the length equal to 20?")
if len(lawn) == 20:
    print("Edward: Yeah Bella. Even if I can't read your mind, you seem smart :P")
elif len(lawn) > 20:
    print("Edward: You dummy! You can't make a good asumption! >o<")
else:
    print("Edward: Yes, You are close to it. However, try adding" + " "+ str(int(len(lawn)+1))+ " " + "with it.")

print("Bella: Well leave it! I know who you are!!")
print("Edward: You do? Then tell me whether my age is a multiple of either 2 or 5. Can you say it Bella?")
age = int(input("Enter Edward's age: "))
if age % 2 == 0 or age % 5 == 0:
    print("Bella: Yes, it multiplies!")
else:
    print("Bella: Sadly, no :(")

print("Edward: You got it right. However, can you identify whether my age is a multiple of either 2 or 5 but not both?")
if age % 2 == 0 and age % 5 == 0:
    print("Bella: Damn! It multiplies by both :0")
elif age % 2 == 0:
    print("Bella: It is only multiplied by 2")
elif age % 5 == 0:
    print("Bella: It is only multiplied by 5.")
else:
    print("Bella: Your age is hopeless. It does not multiplied by either values! >_<")

print("Edward: I must praise you girll <3!")
print("Bella: Don't mention it. Well now, I have a question for you hunky.")
print("Edward: Bring it on :)")
print("Bella: I rate your hair: 10, eyes: 5, friendliness: 0, anger: -5. Now showcase these numbers to me reversely without explicitly writing them.")
print("Edward: Ouch! You are cruel, Bella. But I must praise you for throwing such cute problem.")
x = 10
lst1 = []
while x >= -5:
    lst1.append(x)
    x -= 5

print("Edward: Here is your solution, Bella:")
lst2 = []
for y in range(len(lst1)):
 
    v = lst1[y::-1]
print(v)






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





    

    





   




