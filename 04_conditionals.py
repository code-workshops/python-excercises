"""
Guessing Game

We can give players options using conditionals and comparisons. For example, we might want the player to see certain things
when they turn left or give them a reward if they reach a certain score.
"""
import random

# We'll randomly select a number from 1 to 100. The player must guess this number!
answer = random.randrange(1,101)

# Count the number of times the player gets it wrong
tries = 0
QUIT = False

while not QUIT:
    # Let the player type an answer
    choice = input("Pick a number (1-100): ")

    # Complete the comparisons
    # Replace YOUR_COMPARISON_HERE with an equality
    if YOUR_COMPARISON_HERE:
        print "Too high!"
        tries += 1
    elif YOUR_COMPARISON_HERE:
        print "Too low!"
        # Increment the number of tries below
    elif tries > 3:
        print "Awww, too late ...the answer is:"
        print answer
        QUIT = True
    else:
        print "CORRECT! YOU WIN!"
        QUIT = True
