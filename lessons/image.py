"""
Source: http://www.nerdparadise.com/programming/pygame/part2
"""
import pygame
import os

print "Script start ..."

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
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Color screen background white
    screen.fill((255, 255, 255))

    # Our image -- Look in the left panel and check the images folder for it
    screen.blit(get_image('images/ball.png'), (20, 20))

    pygame.display.flip()
    clock.tick(60)
