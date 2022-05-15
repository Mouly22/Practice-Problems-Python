#An anagram is a play on words created by rearranging the letters of the original word to make a new word or phrase. So we can say two words are anagrams if they contain all of the same letters, but in a different order.
m = 'study'
n = 'dustyyyy'
u = len(m)
v = len(n)
b = 0
z = ''
if u != v:
    z = "They are not anagram"
elif u == v:
    for i in range(v):
        if m[i] == n[i]:
            z = "They are anagram"
        else:
            z = "They are not anagram"
print(z)