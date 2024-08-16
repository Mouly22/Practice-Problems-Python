# Captain Jack and his crew have discovered a treasure chest full of gold coins. However, the chest comes with a mysterious lock.
#  To open it, they need to input a phrase that should contain a combination of characters where vowel count is divisible by 3 and consonant
#  count is divisible by 5. Write a Python program to help Captain Jack determine if the input phrase has the correct number of vowels and 
# consonants to unlock the treasure chest
#       Sample Input              Output
# Yo-hoo-hoo!                   Blimey! No Plunder!!

# Yo-ho-Ya-ho-hoo!              Aaarr! Me Plunder!!

#aoouii-uii                     Blimey! No Plunder!!

inp = input("Enter the Phrase: ")
Vcount = 0
Ccount = 0

for i in range(len(inp)):
    if ord(inp[i]) == 101 or ord(inp[i]) == 97 or ord(inp[i]) == 105 or ord(inp[i]) == 111 or ord(inp[i]) == 117 or ord(inp[i]) == 65 or ord(inp[i]) == 69 or ord(inp[i]) == 73 or ord(inp[i]) == 79 or ord(inp[i]) == 85:
        Vcount += 1
    elif 65 <= ord(inp[i]) <= 90 or 97 <= ord(inp[i]) <= 122 and (ord(inp[i]) != 101 or ord(inp[i]) != 97 or ord(inp[i]) != 105 or ord(inp[i]) != 111 or ord(inp[i]) != 117 or ord(inp[i]) != 65 or ord(inp[i]) != 69 or ord(inp[i]) != 73 or ord(inp[i]) != 79 or ord(inp[i]) != 85):
        Ccount += 1

if Vcount %3 == 0 and Ccount %5 == 0 and (Vcount != 0 and Ccount != 0):
    val = 'Aaarr! Me Plunder!!'
else:
    val = 'Blimey! No Plunder!!' 
print(val)






# 97, 101, 105, 111, 117, 65, 69, 73, 79, 85