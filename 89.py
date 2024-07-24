#rock, paper, scissor
import sys
print("Otis: Hey Maple, Let's play rock, paper and scissor. What say?")
print("Maple: Sure, we can. But can we quickly go through the rules?")
print("Otis: Yup, let's define rock as r, paper as p, scissor as s and quit as q? ")
print("Maple: What should be the limit of this game?")
p1_win= 0
p2_win = 0
p1_tie = 0
p2_tie = 0
thresold = input("Otis: The game limit is: ")

flag = False

for i in range(int(thresold)):
    p1 = input("Otis's choice: ")
    p2 = input("Maple's choice: ")

    if p1 == 'q' or p2 == 'q' or i == int(thresold)-1:
        if p1_win > p2_win:
            print("Otis: I win with "+ str(p1_win)+ " point(s).")
            flag = True
            
        elif p1_win < p2_win:
            print("Otis: Maple, you win with "+ str(p2_win)+ " point(s).")
            flag = True

        elif p1_tie == p2_tie:
            print("Otis: This is a draw match. ")
            flag = True
        else:
            print("Invalid choice! Youu imposter >_<...")
            flag = True
            

    elif (p1 == 'r' and p2 == 'r') or (p1 == 's' and p2 == 's') or (p1 == 'p' and p2 == 'p'):
        p1_tie += 1
        p2_tie += 1
    elif p1 == 'r' and p2 == 'p':
        p2_win += 1
    elif p1 == 'r' and p2 == 's':
        p1_win += 1
    
    elif p1 == 's' and p2 == 'p':
        p1_win += 1
    elif p1 == 's' and p2 == 'r':
        p2_win += 1

    elif p1 == 'p' and p2 == 's':
        p2_win += 1
    elif p1 == 'p' and p2 == 'r':
        p1_win += 1


    if flag == True:
        break








