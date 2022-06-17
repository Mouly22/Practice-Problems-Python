# Suppose you are given a list of contacts as input in single line. Your task is to create a “Phonebook” out of those contacts. The phonebook is nothing but a nested dictionary which is made of 1 rule:
# 1.You have to save each contact based on the starting letter. If there is no contact starting with a specific letter, that letter should not be shown in the phone book.
# While printing the phonebook as output the starting letters should be sorted from A-Z. Also the contacts under each letter should be shown in sorted order based on the contact names. See the sample output for clarification.
# Sample Input:
# Bob 01932342392 Alice 01546734123 Britney 01303544535 Aeron 01723454642 
# Smith 01923457890 Tarek 09663922 Carol 01823456785
# Sample Output: (No need to follow this output format. Just print the 
# resultant dictionary in alphabetical order)
# {A:{ Aeron:01723454642, Alice:01546734123} B:{Bob:01932342392, Britney:01303544535} C: {Carol:01823456785}S: {Smith:01923457890}T: {Tarek:09663922}}
def phonebook(*vals):
    dct = {}
    lst = []
    for i in range(len(vals)//2):
        lst.append([vals[0 + 2*i], vals[1 + 2*i]])
        
    for p in lst:
        a = p[0][:1]
        if a not in dct.keys():
            dct[a] = {p[0] : p[-1]}
        else:
            if p[0] not in dct[a].keys():
                dct[a][p[0]] = p[-1]
    
    print(dct)
    
    
phonebook('Bob', '01932342392', 'Alice', '01546734123', 'Britney', '01303544535', 'Aeron', '01723454642', 'Smith', '01923457890', 'Tarek', '09663922', 'Carol', '01823456785')
         