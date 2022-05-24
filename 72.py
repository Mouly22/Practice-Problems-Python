# Write a function called individul_bonus_calculation which will take 4 arguments. They are:
# The player name
# Yearly earning of that player
# The total goal scored this season by that player
# Bonus percent per goal.
# Your task is to implement the above-mentioned function that will calculate the total bonus on the yearly earnings of a player for the total goals he had scored.
# Additionally,
# If the goal scored is above 30, add a (additional) bonus of 10000 taka.
# If it is between 20 and 30 inclusive, add an extra 5000 taka.
# Example1:
# individul_bonus_calculation("Neymar", 1200000, 35, 5)
# bonus = 35 * (5 / 100 * 1200000) + 10000 = 2110000
# Function call: individul_bonus_calculation("Neymar", 1200000, 35, 5)
# Output: Neymar earned a bonus of 2110000 Taka for 35 goals.
# Example2:
# individul_bonus_calculation('Jamal', 700000, 19, 8)
# bonus = 19 * (8 / 100 * 700000) + 0 = 1064000
# Function call: individul_bonus_calculation('Jamal', 700000, 19, 8)
# Output: Jamal earned a bonus of 1064000 Taka for 19 goals.
# Example3:
# individul_bonus_calculation('Luis', 80000, 25, 10)
# bonus = 25 * (10 / 100 * 80000) + 5000 = 205000
# Function call: individul_bonus_calculation('Luis', 80000, 25, 10)
# Output: Luis earned a bonus of 205000 Taka for 25 goals.
def individul_bonus_calculation(p_name, y_ern, t_goal, g_bonus):
    if t_goal > 30:
        x = 10000
    elif t_goal > 20 and t_goal <= 30:
        x = 5000
    else:
        x = 0
    bonus = t_goal*((g_bonus/100)*y_ern) + x
    print(f"{p_name} earned a bonus of {bonus} Taka for {t_goal} goals.")
    
individul_bonus_calculation('Jamal', 700000, 19, 8)