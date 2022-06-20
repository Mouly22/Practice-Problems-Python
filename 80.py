# Suppose you are given a list of contacts as input in single line. Your task is to create a “Phonebook” out of those contacts based on their telecom operator. The phonebook is nothing but a nested dictionary which is made of 1 rule:
# 1.You have to save each contact based on their telecom operator. If there is no contact of a specific telecom operator, that operator should not be shown in the phone book. If a contact number,
# Starts with ‘017’ or ‘013’ then the telecom operator is Grameenphone
# Starts with ‘018’ then the telecom operator is Robi
# Starts with ‘016’ then the telecom operator is Airtel
# Starts with anything else then the telecom operator is Others
# While printing the phonebook as output the contacts under each telecom operator should be shown in alphabetically sorted order based on the contact names. See the sample output for clarification.
# Sample Input:
# Bob 01632342392 Alice 01346734123 Britney 01803544535 Aeron 01723454642 Smith 01923457890 Tarek 01866392233
# Sample Output:(No need to follow this output format. Just print the resultant sorted dictionary. )
# { Airtel: { Bob:01632342392} Grameenphone: { Aeron:01723454642 Alice:01346734123 } Robi: { Britney:01803544535 Tarek:01866392233 }
# Others:{Smith:01923457890}}
def phone(*contacts):
    lst = []
    dct = {}
    for i in range(len(contacts)//2):
        lst.append([contacts[0+2*i], contacts[1+2*i]])
    for i in lst:
        if '017' in i[-1] or '013' in i[-1]:
            a = "Grammenphone"
        elif '018' in i[-1]:
            a = "Robi"
        elif '016' in i[-1]:
            a = "Airtel"
        else:
            a = "Others"
        
        if a not in dct.keys():
            dct[a] = {i[0] : i[-1]}
        else:
            if i[0] not in dct[a].keys():
                dct[a][i[0]] = i[-1]
            

    print(dct)  
    
phone('Bob','01632342392', 'Alice', '01346734123', 'Britney', '01803544535', 'Aeron', '01723454642', 'Smith', '01923457890', 'Tarek', '01866392233')
