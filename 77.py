# In a given string, there will be two uppercase letters in between some lowercase letters.
#  Print the substring from the first uppercase letter to the last uppercase letter excluding them. If there are no letters in between them, print the word BLANK. It is guaranteed that there will be only two uppercase letters in the string.
# Sample Input      Sample Output
# baNgladEsh        glad
# coDIng            BLANK
k = 'coDing'
count1 = 0
count2 = 0
g = ''
oh =''
ls = []
for i in range(len(k)):
    if k[i] == k[i].upper():
        count1 += 1
        if count1 == 1:
            g = k[i+1:]
            
for j in range(len(g)):
    if g[j] == g[j].upper():
        count2 += 1
        if count2 == 1:
            oh = g[:j]
            if oh == '':
                oh = "BLANK"
            else:
                oh = g[:j]
        else:
            oh = "Somthing's wrong. Please check again."
            
print(oh)