# You have been hired by the Abahani football club to write a function that will calculate the total bonus on the yearly earnings of each player for the total goals they have scored.
# Since the number of players will vary, you decide to use the "*args" technique that you learned in your CSE110 class.
# For each player: pass the name, yearly earning, the total goal scored this season, bonus percent per goal.
# Additionally,
# If the goal scored is above 30, add an extra bonus of 10000 taka.
# If it is between 20 and 30 inclusive, add an extra 5000 taka.
# Example1:
# cal_bonus("Neymar", 1200000, 35, 5)
# bonus = 35 * (5 / 100 * 1200000) + 10000 = 2110000
# Function call:   
# cal_bonus("Neymar", 1200000, 35, 5)
# Output:    
# Neymar earned a bonus of 2110000 Taka for 35 goals.
# Example2:
# Function call:
# function_name("Neymar", 1200000, 30, 10, "Jamal", 700000, 19, 5)
# Output:
# Neymar earned a bonus of 3605000 Taka for 30 goals.
# Jamal earned a bonus of 665000 Taka for 19 goals.
# Example3:
# Function call:
# function_name("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10))
# Output:
# Neymar earned a bonus of 2110000 Taka for 35 goals.
# Jamal earned a bonus of 1064000 Taka for 19 goals.
# Luis earned a bonus of 205000 Taka for 25 goals.
def individul_bonus_calculation(*args):
    lst = []
    for k in range((len(args))//4):
        lst.append([ args[0+4*k],args[1+4*k],args[2+4*k],args[3+4*k] ])       #appending a list inside another list
        if args[2+4*k] > 30:
            x = 10000
        elif args[2+4*k] > 20 and args[2+4*k] <= 30:
            x = 5000
        else:
            x = 0
        bonus = args[2+4*k] *((args[3+4*k]/100)* args[1+4*k]) + x
        
        print(f"{args[0+4*k]} earned a bonus of {bonus} Taka for {args[2 + 4*k]} goals.")
              
individul_bonus_calculation("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10)