"""
Pygame Structure

A Pygame is basically structured in 3 parts:
    * Events
    * Loop
    * Render

Within the main game loop, those 3 events should be executed in that order. See code
comments below for explicit detail.

Source: http://www.nerdparadise.com/programming/pygame/part1
"""
import pygame

# Initialize the game engine
pygame.init()

# Set game screen size
screen = pygame.display.set_mode((400, 300))

# Off switch for the game
done = False

# Controls the color of the square on screen when spacebar is pressed
is_blue = True

# Starting location of the square
x = 300
y = 30

# A throttling tool to control fps
clock = pygame.time.Clock()


print "Game starting ..."

# Main game loop
while not done:
    #####################################################
    # STEP 1: EVENTS
    # Check for new events such as movement and closing
    ######################################################

    # Loop through all game events
    for event in pygame.event.get():
        # If the player quits ...
        if event.type == pygame.QUIT:
            done = True
        # If the spacebar is pressed, toggle the status of the square
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    ################################################
    # STEP 2: GAME LOOP
    # Code below will repeat until the game ends!
    ################################################

    # Validator for key presses
    pressed = pygame.key.get_pressed()

    # If the arrow keys are pressed, move the box around
    # if pressed[pygame.K_UP]: y -= 3
    # if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    # Change the color of the square based on the is_blue condition
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    ##########################################################
    # STEP 3: RENDER
    # Finish up by drawing all the objects to the game world
    ##########################################################

    # Set the background color of screen
    screen.fill((0, 0, 100))

    # Draw the square on the screen
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    # Throttle to 60fps to slow down events on the screen
    clock.tick(60)
