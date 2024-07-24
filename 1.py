#A conversation
print("Hey There! What's your name?")
name1 = input("Enter your name:" )
print("My name is" + " " +name1+ ", " + "and Yours?")
name2 = input("Enter your name:" )
print("I am"+ " "+ name2 + ". "+ "Nice to meet you.")
print("R: Do you want to grab a cup of coffee sometimes?")
print("M: Yeah, sure!")
print("R: I am facing some problem with calculating the gross pay value, do you mind helping me?")
print("M: For sure. Tell me.")
print("R: I am planning to compute the gross pay by providing the working hours and a rate for per hour of usage. I am planning to decide a centain thresold to increase the pay 1.5 times. Can you help me with a number?")
thresold_value = int(input("Enter thresold value: "))
print("M: Let's decide the number as "+ str(thresold_value))
print("R: Let's assign conditions to fulfill these criterias. Shall we?")
hour_input = float(input("Enter your working hour: "))
per_hour_input = float(input("Enter assigned rate for each working hour: "))
if hour_input > thresold_value:
    extraHour = (hour_input - thresold_value) * 1.5
    normalHour = (thresold_value  + extraHour) * per_hour_input
else: 
    extraHour = 0
    normalHour = hour_input * per_hour_input + extraHour
print("M: I guess this program will provide you your desirable answer.")
print("R: Let's Check?")
print("M: Your desired output is: " + str(normalHour))
print("R: Perfect, Thanks a lot!")
print("M: Now, it's time for us to grab that promised coffee.")
print("R: Ofcourse. My Treat..!")
print("M: Okay, but next time my turn. Okay?")
print("R: Sure <3")