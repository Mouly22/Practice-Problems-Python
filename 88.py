#Guess the number game.
print("Jaber: Hey there, are you interested in playing a number guessing game?")
print("Kabir: Yeah, sure. Provide me a range to guess?")
print("Jaber: Guess a number between 1 to 20. If you guess it right, I have a gift for you.")
number = int(input("Kabir: I am guessing: "))
count = 0
while True:
    thresold = 14


    if number >= 0 and number < thresold:
        number = int(input("Kabir: Your guess is too low. Guess again: "))
        count += 1
    elif number > thresold and number <=20:
        number = int(input("Kabir: Your guess is too high. Guess again: "))
        count += 1
    elif number == thresold:
        count +=1
        print("Kabir: Your guess is correct. You guessed my number in "+ str(count)+ " guess(es).")
        break
    else:
        number = int(input("Kabir: Invalid. Guess again: "))
        count += 1
        