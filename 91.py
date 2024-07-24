#Collatz sequence!

def collatz(num):

    while True:

        if num == 1:
            break
    
        elif num % 2 == 0:
            num = num //2
            print(num)
          
            
        elif num % 2 == 1:
            num = 3* num + 1
            print(num)

   
number = int(input("Enter a Number: "))
collatz(number)
    


        
