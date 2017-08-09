"""
Guessing Game 2.0

We can give players options using conditionals and comparisons. For example, we might want the player to see certain things
when they turn left or give them a reward if they reach a certain score.
"""
import random

# We'll randomly select a number from 1 to 100. The player must guess this number!
answer = random.randrange(1, 26)

# Count the number of times the player gets it wrong
tries = 0
GAME_ON = True

while GAME_ON:
    # Let the player type an answer
    choice = input("Pick a number (1-25): ")

    # Complete the comparisons
    # Replace YOUR_CONDITION_HERE with an equality
    if YOUR_ CONDITION_HERE:
        print "Too high!"
        tries += 1
    elif YOUR_CONDITION_HERE:
        print "Too low!"
        # Increment the number of tries below
        YOU_FORGOT_TO_INCREMENT_TRIES
    else:
        print "CORRECT! YOU WIN!"
        break

    # After the player has played, check that they haven't tried more than 3 times!
    if YOUR_CONDITION_HERE:
        print "Too many tries! The answer is: ", answer
        GAME_ON = False