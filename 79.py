# As a software engineer, you are hired to arrange football players based on their country and position. You have given all the player’s information in a tuple called my_tuple. The players are from 3 countries which are Brazil, Argentina and Germany. They are 2 positions which are “Forward” and “Midfield”
# You are given the following nested tuple where each element in the my_tuple is a tuple consisting of a name and a 4 digit ID.
# my_tuple = (("Firmino", 1101),("Gabriel", 1201),("Casemiro", 1302),
# ("Fred", 1402),("Messi", 1111),("Aguero", 1211),("Klose", 1121), ("Werner", 1221), ("Toni", 1322))
# Write a python program that will convert this tuple into the following dictionary using the process described below:
# Your code should work for all types of similar tuple if the sample input is changed.
# Output dictionary (You just have to print the resultant dictionary. No need to follow the pattern below):
# {
# 'Forward':
#  {
#  'Brazil': ('Firmino', 'Gabriel'),
#  'Argentina': ('Messi', 'Aguero'),
#  'Germany': ('Klose', 'Werner')
#  }
# 'Midfielder':
#  {
#  'Brazil': ('Casemiro', 'Fred')
#  'Germany': 'Toni'
#  }
# }
# CONTINUATION:
# Here you need to convert the given tuple into the output using the 4 digit 
# ID. The rules are given below:
# 1==> Last digit of the ID represents the position. Here
#  1a--> 1 means Forward
#  1b--> 2 means Midfield
# 2==> Third digit of the ID represents the country. Here
#  2a--> 0 means Brazil
#  2b--> 1 means Argentina
#  2c--> 2 means Germany
# 3==> If you have multiple players in a category use tuple to store the multiple names as the value of the nested dictionary
# 4==> If any country has no player of a particular position, that country name should not appear as a key in the nested dictionary of that particular position. For example, Argentina has no midfielder. So Argentina did not appear under the “Midfield” position.
# 5==> If your output dictionary’s key value pair sequence is not the same as the shown output you should not worry about that. However, the key value pair should be exactly the same
def mtuple(*args):
    dct = {}
    for i in args:
        a = str(i[1])
        b = a[-1]
        if b == '1': 
            place ="Forward"
        elif b == '2':
            place ="Midfielder"
        c = a[-2]
        if c == '0':
            cou = "Brazil"
        elif c == '1':
            cou = "Argentina"
        elif c == '2':
            cou = "Germany"

            
        if place not in dct.keys():
            dct[place] = {cou : [i[0]]}
        else:
            if cou not in dct[place].keys():
                dct[place][cou] = [i[0]]
                
            else:
                dct[place][cou].append(i[0])
      
    for key, val in dct.items():
        for k,v in val.items():
            dct[key][k] = tuple(v)
                
    print(dct)
            
            

        
mtuple(("Firmino", 1101),("Gabriel", 1201),("Casemiro", 1302), ("Fred", 1402),("Messi", 1111),("Aguero", 1211),("Klose", 1121), ("Werner", 1221), ("Toni", 1322))