"""
Draw
====

A simple pygame demonstration of painting on screen with a mouse!

Source: http://www.nerdparadise.com/programming/pygame/part6
"""
import pygame


def play():
    """
    Functions are objects that execute a sequence of commands.

    Here's how to play this game:
        * Use the mouse to paint
        * Use the left mouse button to make the brush bigger
        * Use the right mouse button to make the brush smaller
        * Use r, g, or b keys to change the colors
        * Use ESCAPE to quit

    :return:
    """

    # Initialize pygame
    pygame.init()

    # Setup screen size
    screen = pygame.display.set_mode((640, 480))

    # Create a timer
    clock = pygame.time.Clock()

    # Define the size of our cursor
    radius = 15

    # Coordinates to track the position of the mouse
    x = 0
    y = 0
    mode = 'blue'
    points = []

    # Game loop
    while True:

        # Track the keys pressed during game play
        pressed = pygame.key.get_pressed()

        # Assign the ALT and CTRL keystrokes to a variable
        # There are usually a right and left ALT and CTRL so we track both
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # To quit use: X or Ctrl+W or Alt+F4 or just lose the game window
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                # ############################
                # PRACTICE
                # --------
                #
                # Add a new keypress that will close the game: pygame.K_Q

                # Allow player to control the color of the ink with the r, g or b keys
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

            # Allow player to use the mouse buttons to change paint brush size
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Make brush larger
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    # Make brush smaller
                    radius = max(1, radius - 1)

            # When the mouse moves, collect all the points into a list
            if event.type == pygame.MOUSEMOTION:
                position = event.pos            # The current mouse position
                points = points + [position]    # The points from mouse movement
                points = points[-256:]          # The current point forward

        # Screen background color
        screen.fill((0, 0, 0))

        # Index counter for stopping the next loop
        i = 0

        # Draw all the points from the mouse positions defined above
        while i < len(points) - 1:
            # Call our drawLineBetween function to paint!
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    """
    This function drows the brush strokes between points onto the screen

    Here's a breakdown of what each of the above arguments does
    :param screen: pygame background screen
    :param index: current mouse point
    :param start: point to begin painting from
    :param end: next point to paint
    :param width: the size of our brush
    :param color_mode: current player selected color
    :return:
    """
    # Define the RGB color codes which range from 0 to 255
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    # Match the color_mode variable to the right color code
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    # Points on the screen for the brush strokes
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in xrange(iterations):
        progress = 1 * i / iterations
        aprogress = 1 - progress
        x = aprogress * start[0] + progress * end[0]
        y = aprogress * start[1] + progress * end[1]

        # Finally, we draw our brush strokes!
        pygame.draw.circle(screen, color, (x, y), width)

# Start the game by calling the game function
play()