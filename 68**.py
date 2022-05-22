# Write a function which will take 2 arguments. They are:
# Sentence
# position
# Your first task is to take these arguments as user input and pass these values to the function parameters.
# Your second task is to implement the function and remove the characters at the index number which is divisible by the position (Avoid the index number 0 as it will always be divisible by the position, so no need to remove the index 0 character). Finally, add the removed characters at the end of the new string.
# Return the value and then finally, print the new string at the function call.
# [Cannot use remove() or removed() for this task]
# Input 1: 
# "I love programming."
# 3
# Function call: function_name("I love programming.", 3)
# Output 1: I lveprgrmmngo oai.
# Input 2:
# "Python is easy to learn. I love python."
# 6
# Function call: function_name("Python is easy to learn. I love python.", 6)
# Output: Pythonis eay to earn.I lov pythn. sl eo
p = 'Python is easy to learn. I love python'
z = []
v =[]
q = 6
count = 0
for i in range(len(p)):
    count = i
    if count >= 1:
        if count % q != 0:
            z.append(p[i])
        elif p[i] != p[0]:
            v.append(p[i])
    elif count == 0:
        z.append(p[0])
w = z + v
for i in w:
    n = ''.join(w)

print(n)