# Write a python program that takes a sentence from the user which is separated by space. Now you have to reverse the character of every single word without reversing the sentence itself. You cannot change the position of the word.
# Input 1: My name is Anwar    Output 1: yM eman si rawnA
# Input 2: I am a student      Output 2: I ma a tneduts
c = "My name is Anwar".split(" ")
z =[]
m = ''
for i in range(len(c)):
    g = c[i]
    k = g[-1::-1]
    z.append(k) 
    
for d in z:
    m = ''.join(str(d))
    print(m, end = " ")