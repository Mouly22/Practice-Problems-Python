print("M: Number of Chocolates, N: Number of empty packets, P: Number of new chocolates")

M = int(input("Enter initial chocolate amount: "))
N = int(input("Enter number of empty packets to get a new chocolate: "))
P = int(input("Enter number of new chocolate(s) correspond to empty packets: "))
Tchoco = M

while True:
    
    if M % N == 0:
        newChoco = M // N
        M = newChoco * P
        empPacket = newChoco * P
        Tchoco += M
    else: 
        if empPacket < N:
            print("Chocolates in Total: "+str(Tchoco))
            
            break
        else:
            
            newChoco = M // N 
            leftPacket = M % N
        
            empPacket = newChoco * P + leftPacket
            M = empPacket * P
            Tchoco += newChoco * P
    
    
       


