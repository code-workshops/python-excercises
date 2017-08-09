"""
Guessing Game 2.0

We can give players options using conditionals and comparisons. For example, we might want the player to see certain things
when they turn left or give them a reward if they reach a certain score.
"""
import random

# We'll randomly select a number from 1 to 25. The player must guess this number!
answer = random.randrange(1, 25)

# Count the number of times the player gets it wrong
tries = 1
GAME_ON = True

while GAME_ON:
    # Let the player type an answer
    choice = int(input("Pick a number (1-25): "))

    # Complete the comparisons
    # Replace YOUR_COMPARISON_HERE with an equality
    if answer == choice:
        print "CORRECT! YOU WIN!"
        break
    elif tries >= 3:
        print "Too many tries! The answer is: ", answer
        GAME_ON = False
    elif choice > answer:
        print "Too high!"
        tries += 1
    else:
        print "Too low!"
        # Increment the number of tries below
        tries += 1
