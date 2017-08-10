"""
Source: http://www.nerdparadise.com/programming/pygame/part2
"""
import pygame
import os

_image_library = {}


def get_image(path):
    """
    A function that searches for our image and returns it.

    :param path: the location of the image file
    :return:
    """
    global _image_library
    image = _image_library.get(path)
    if not image:
        new_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(new_path)
        _image_library[path] = image

    # Make a new line below and add a print statement

    return image


# Start game engine
pygame.init()

# Create a screen that's 400px x 300px
screen = pygame.display.set_mode((400, 300))
GAME_ON = True
clock = pygame.time.Clock()

while GAME_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GAME_ON = False

    # Color screen background white
    screen.fill((255, 255, 255))

    # Our image -- Look in the left panel and check the images folder to find it
    # This is called the 'path' to the image. It names the folder its in and its name.
    screen.blit(get_image('media/orb.png'), (20, 20))

    pygame.display.flip()
    clock.tick(60)
