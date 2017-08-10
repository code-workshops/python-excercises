"""
Review 1: Python Basics
-----------------------

Let's say we are making a game. First we need to do the following:
    - Draw the player onto the screen
    - Setup the keypresses to move the player around

You should copy code from earlier lessons to help you out. Your game should:
    1. Have a function
    2. Use variables
    3. Include a game loop

Here's some code to get you started!
"""
import pygame

# Initialize the game engine
pygame.init()

# Set game screen size
screen = pygame.display.set_mode((400, 300))

# Off switch for the game
GAME_ON = True

# A throttling tool to control fps
clock = pygame.time.Clock()

# REMEMBER: ALL CODE SHOULD BE WITHIN THE FUNCTION!


# 1 - Create a function named play() below

# 2 - Add a game loop using the GAME_ON condition

# 3 - Write a for loop to loop through game events and key presses
# HINT: for event in pygame.event.get() ...

# 4 - Draw the screen background

# 5 - Draw the player image onto the screen
# HINT: screen.blit(image_name, (width, height))

pygame.display.flip()

# 6 - Call the play() function
