# Write a python function that takes a string as an argument. Your task is to calculate the number of uppercase letters and lowercase letters and print them in the function.
# Function Call: function_name('The quick Sand Man')
# Output:
# No. of Uppercase characters : 3
# No. of Lowercase Characters: 12

# Function Call: function_name('HaRRy PotteR')
# Output:
# No. of Uppercase characters : 5
# No. of Lowercase Characters: 6
def function_name(p):
    sc = 0
    bc = 0
    for i in p:
        if  ord(i)>= 65 and ord(i) <= 90:
            bc = bc + 1
            c = bc
        elif ord(i)>= 97 and ord(i) <= 122:
            sc = sc + 1
            d = sc
    print(f"No. of Uppercase characters :",c)
    print(f"No. of Lowercase Characters:", d)
function_name('The quick Sand Man')