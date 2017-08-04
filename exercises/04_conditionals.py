"""
Guessing Game

We can give players options using conditionals and comparisons. For example, we might want the player to see certain things
when they turn left or give them a reward if they reach a certain score.
"""
import random

# We'll randomly select a number from 1 to 100. The player must guess this number!
answer = random.randrange(1, 26)

# Let the player type an answer
choice = input("Pick a number (1-25): ")

# Complete the comparisons
# Replace YOUR_COMPARISON_HERE with an equality
if YOUR_COMPARISON_HERE:
    print "Too high! You lose!"
elif YOUR_COMPARISON_HERE:
    print "Too low! You lose!"
else:
    print "CORRECT! YOU WIN!"
    break
