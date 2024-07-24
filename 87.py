#An annoying guy who keeps on asking your name
print("Stranger: Hey Gal! Can I have your name?")
print("Girl: No, stranger! Get off of me.")
print("Stranger: I ain't leaving unless I have your name!")
name = input("Your Name?: ")

while name != "Lily":
    print("That's not your name! Please tell me your actual name :')" )
    name = input("Say it again?: ")
    if name == "Lily":
        break
print("Thanks "+ name +".")
                                                   
#Girl planning to login to her PC
nm1 = input("Please enter your name: ")
while nm1 != "Lily":
    if nm1 == "lily":
        nm1 = input("PC: You are one character away to make it work! Try again:")
    elif nm1 == "l":
        nm1 = input("PC: That's not even funny :).. Try again: ")
    else:
       nm1 = input("PC: Wrong Username. Try providing Correct Username: ")
print("PC: Hey "+  nm1+", ^_^" +" Please provide your Password...")
var = ''
password = input("Enter your password: ")

for i in range(2, -1, -1):
    if password != "Billybo1920":
        password = input("PC: Wrong Password! You can take "+ str(i)+ " more attempts to Enter a Correct Password: ")
        if password == "Billybo1920":
            print("PC: Welcome Abroad, "+nm1)
            break
        elif i <= 0:
            print("PC: Access Denied. Sorry Imposter.. :P ")
        else: 
            pass
    else:
        var ="PC: Welcome Abroad, " + nm1
print(var)
 




