"""
Source: http://www.nerdparadise.com/programming/pygame/part4
"""
import pygame

# FIRST: Define our functions


def make_font(fonts, size):
    # Find the available fonts in the pygame.font module
    available = pygame.font.get_fonts()

    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x: x.lower().replace(' ', ''), fonts)

    # for loop checks each choice from our choices object defined above
    for choice in choices:
        if choice in available:
            # TODO: Whats the difference between Font and SysFont?
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)

_cached_fonts = {}


def get_font(font_preferences, size):
    global _cached_fonts
    # Create a name for font so we can save it and use it later
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    # This means: 'if there is no font then create one'
    if not font:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

_cached_text = {}


def create_text(text, fonts, size, color):
    global _cached_text
    # TODO: This can't be right. Test the key names here and in get_font()
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    # Condition: 'if there is no image, create a new one'
    if not image:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image

# Start game engine
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

font_preferences = [
        "Bizarre Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]

text = create_text("Hello, World", font_preferences, 72, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)