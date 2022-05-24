#Write a python program that splits a given string on a given split character. The first input is a String and the second input is the character that will be used to split the first String. [You cannot use the built-in split function]
x = "tom@gmail,harry@yahoo,bob@gmail,mary@gmail"
y = ","
z = ''
for i in range(len(x)):
    z = x.replace(y[0]," \n")
print(z)